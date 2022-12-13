from rest_framework import serializers
from drive_backend.file_system.models import File, Folder

class FileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['name', 'file', 'folder']

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'