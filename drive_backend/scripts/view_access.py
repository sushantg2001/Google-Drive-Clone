
from drive_backend.file_system.models import File, Folder
from drive_backend.file_system.api.serializers import FileDetailSerializer, FolderSerializer
from django.db.models import Q
def run():
    folder = Folder.objects.get(id=9)
    test = folder.access.filter(user__id = 5)
    print(test.values())
