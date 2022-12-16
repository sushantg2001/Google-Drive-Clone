from rest_framework import serializers
from drive_backend.file_system.models import File, Folder, FileAccess, FolderAccess
from drive_backend.users.api.serializers import UserDetailSerializer

class FileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ['users']

class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['name', 'file', 'parent', 'id']

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        exclude = ['users']

class FileAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAccess
        fields = ['file', 'type', 'user']

class FolderAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderAccess
        fields = ['folder', 'type', 'user']
