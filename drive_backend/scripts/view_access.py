
from drive_backend.file_system.models import File, Folder
from drive_backend.file_system.api.serializers import FileDetailSerializer, FolderSerializer
from django.db.models import Q
def run():
    folder = Folder.objects.get(id=1)
    test = folder.access.filter(Q(user__id = 1) & Q(type = 'viewer')).exists()
    print(test)
