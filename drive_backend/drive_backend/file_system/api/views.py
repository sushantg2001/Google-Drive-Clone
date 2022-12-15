from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin,UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drive_backend.file_system.models import File, Folder
from drive_backend.users.models import User
from .serializers import FileDetailSerializer, FileUpdateSerializer, FolderSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from django.db.models import Q
from drf_multiple_model.mixins import ObjectMultipleModelMixin
from rest_framework.exceptions import PermissionDenied

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsEditor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if IsOwner.has_object_permission(self, request, view, obj) or obj.access.filter(Q(user = request.user) & Q(type = 'editor')).exists():
            return True
        return False

class IsViewer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if IsEditor.has_object_permission(self, request, view, obj) or obj.access.filter(Q(user = request.user) & Q(type = 'viewer')).exists():
            return True
        return False

class FileViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = File.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        if self.action == 'partial_update' and self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsEditor]
        if self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsViewer]
        if self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return FileUpdateSerializer
        return FileDetailSerializer

class FolderViewSet(RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet, DestroyModelMixin):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        if self.action == 'partial_update' and self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsEditor]
        if self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsViewer]
        if self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.parent.id == '0':
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().destroy(request, *args, **kwargs)

class FilesandFolders(ObjectMultipleModelMixin, GenericViewSet):
    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsViewer]
        return [permission() for permission in self.permission_classes]

    def get_querylist(self):
        parent = self.request.query_params.get('folder')
        folder = Folder.objects.get(id=parent)
        self.check_object_permissions(request=self.request, obj=folder)
        querylist = [
            {
                'queryset': File.objects.filter(folder=parent), 'serializer_class': FileDetailSerializer,
                'queryset': Folder.objects.filter(parent=parent), 'serializer_class': FolderSerializer
            }
        ]
        return querylist