from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin,UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drive_backend.file_system.models import File, Folder
from drive_backend.users.models import User
from .serializers import FileSerializer, FolderSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class FileViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        if self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()


    def get_serializer_class(self):
        if self.action == 'partial_update':
            per

class FolderViewSet(RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = FileSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)