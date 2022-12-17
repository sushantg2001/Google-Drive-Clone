from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drive_backend.file_system.models import File, Folder, FileAccess, FolderAccess
from drive_backend.users.models import User
from .serializers import (
    FileDetailSerializer,
    FileUpdateSerializer,
    FolderSerializer,
    FileAccessSerializer,
    FolderAccessSerializer,
)
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from django.db.models import Q
from drf_multiple_model.mixins import ObjectMultipleModelMixin
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.views import APIView


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return obj.owner == request.user
        except:
            try:
                return obj.folder.owner == request.user
            except:
                return obj.file.owner == request.user

class IsEditor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if (
            IsOwner.has_object_permission(self, request, view, obj)
            or obj.access.filter(Q(user=request.user) & Q(type="editor")).exists()
        ):
            return True
        return False


class IsViewer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if (
            IsEditor.has_object_permission(self, request, view, obj)
            or obj.access.filter(Q(user=request.user) & Q(type="viewer")).exists()
        ):
            return True
        return False


class FileViewSet(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet, CreateModelMixin
):
    queryset = File.objects.all()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        if self.action == "partial_update" and self.action == "update":
            self.permission_classes = [IsAuthenticated, IsEditor]
        if self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, IsViewer]
        if self.action == "destroy":
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if (
            self.action == "partial_update"
            or self.action == "create"
            or self.action == "update"
        ):
            return FileUpdateSerializer
        return FileDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class FolderViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    DestroyModelMixin,
):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        if self.action == "partial_update" and self.action == "update":
            self.permission_classes = [IsAuthenticated, IsEditor]
        if self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, IsViewer]
        if self.action == "destroy":
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.parent.id == "0":
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class FileAccessViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    DestroyModelMixin,
):
    serializer_class = FileAccessSerializer
    queryset = FileAccess.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        user_id, folder_id = self.kwargs[self.lookup_field].split("-")
        filter_kwargs = {}
        filter_kwargs["user"] = User.objects.get(id=user_id)
        filter_kwargs["file"] = File.objects.get(id=folder_id)
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if (
            self.action == "create"
            or self.action == "partial_update"
            or self.action == "update"
            or self.action == "destroy"
        ):
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]


class FolderAccessViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    DestroyModelMixin,
):
    serializer_class = FolderAccessSerializer
    queryset = FolderAccess.objects.all()
    lookup_field = "slug"

    def recursive_access_share(self, folder, data):
        files_in_folder = File.objects.filter(parent = folder)
        folders_in_folder = Folder.objects.filter(parent = folder)
        for file in files_in_folder:
            obj =  FileAccess.objects.filter(file = file, user = User.objects.get(id=data['user']))
            if obj.exists():
                obj.update(type=data['type'])
            else:
                FileAccess.objects.create(file=file, user = User.objects.get(id=data['user']), type=data['type'])


        for child_folder in folders_in_folder:
            obj =  FolderAccess.objects.filter(folder = child_folder, user = User.objects.get(id=data['user']))
            if obj.exists():
                obj.update(type=data['type'])
            else:
                FolderAccess.objects.create(folder=child_folder, user = User.objects.get(id=data['user']), type=data['type'])

        for child_folder in folders_in_folder:
            self.recursive_access_share(child_folder, data)

    def recursive_access_remove(self, folder, user):
        files_in_folder = File.objects.filter(parent=folder)
        folders_in_folder = Folder.objects.filter(parent=folder)
        for file in files_in_folder:
            file_access = FileAccess.objects.filter(Q(file=file) & Q(user=user)).first()
            if file_access is not None:
                file_access.delete()

        for child_folder in folders_in_folder:
            folder_access = FolderAccess.objects.filter(Q(folder=child_folder) & Q(user=user)).first()
            if folder_access is not None:
                folder_access.delete()

        for child_folder in folders_in_folder:
            self.recursive_access_remove(child_folder, user)

    def get_object(self):
        queryset = self.get_queryset()
        user_id, folder_id = self.kwargs[self.lookup_field].split("-")
        filter_kwargs = {}
        filter_kwargs["user"] = User.objects.get(id=user_id)
        filter_kwargs["folder"] = Folder.objects.get(id=folder_id)
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if (
            self.action == "create"
            or self.action == "partial_update"
            or self.action == "update"
            or self.action == "destroy"
        ):
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        obj = serializer.save()
        folder = obj.folder
        data = serializer.data
        data.pop('folder')
        self.recursive_access_share(folder, data)

    def perform_update(self, serializer):
        obj = serializer.save()
        folder = obj.folder
        data = serializer.data
        data.pop('folder')
        self.recursive_access_share(folder, data)

    def perform_destroy(self, instance):
        self.recursive_access_remove(instance.folder, instance.user)
        instance.delete()

class SharedWithMe(ObjectMultipleModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_querylist(self):
        type = self.request.query_params.get("type")
        print(self.request.query_params)
        files_list = self.request.user.files.all()
        folders_list = self.request.user.folders.all()
        if type is not None and type == "files":
            return [
                {
                    "queryset": files_list,
                    "serializer_class": FileDetailSerializer,
                }
            ]
        elif type is not None and type == "folders":
            return [
                {"queryset": folders_list, "serializer_class": FolderSerializer}
            ]
        else:
            return [
                {"queryset": files_list, "serializer_class": FileDetailSerializer},
                {
                    "queryset": folders_list,
                    "serializer_class": FolderSerializer,
                },
            ]


class FilesandFolders(ObjectMultipleModelMixin, GenericViewSet):
    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsViewer]
        return [permission() for permission in self.permission_classes]

    def get_querylist(self):
        parent = self.request.query_params.get("folder")
        folder = Folder.objects.get(id=parent)
        self.check_object_permissions(request=self.request, obj=folder)
        querylist = [
            {
                "queryset": File.objects.filter(parent=parent),
                "serializer_class": FileDetailSerializer,
                "queryset": Folder.objects.filter(parent=parent),
                "serializer_class": FolderSerializer,
            }
        ]
        return querylist
