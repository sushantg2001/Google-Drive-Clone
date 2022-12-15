
from drive_backend.file_system.models import File, Folder
from drive_backend.users.models import User
from drive_backend.file_system.api.serializers import FileDetailSerializer, FolderSerializer
from django.db.models import Q

def run():
    test_user_folder = File.objects.filter(id=6).first()