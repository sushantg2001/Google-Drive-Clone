from drive_backend.file_system.models import File, Folder
from drive_backend.file_system.api.serializers import FileDetailSerializer, FolderSerializer

def run():
    file_list = File.objects.filter(folder=1)
    data = FileDetailSerializer(file_list, many=True)
    print(data.data)
