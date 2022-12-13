from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin,UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drive_backend.file_system.models import File, Folder
from drive_backend.users.models import User
from .serializers import FileDetailSerializer, FileUpdateSerializer, FolderSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.db.models import Q

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsEditor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if IsOwner.has_object_permission(request, view, obj) or obj.users.filter(Q(user = request.user) & Q(type = 'editor')).exists():
            return True
        return False

class IsViewer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if IsEditor.has_object_permission(request, view, obj) or obj.users.filter(Q(user = request.user) & Q(type = 'viewer')).exists():
            return True
        return False

class FileViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = File.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        if self.action == 'partial_update' and self.action == 'update':
            permission_classes = [IsAuthenticated, IsEditor]
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsViewer]
        if self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return FileUpdateSerializer
        return FileDetailSerializer

class FolderViewSet(RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = FolderSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)