from drive_backend.file_system.api.serializers import FileAccessSerializer
from drive_backend.file_system.models import FileAccess

def run():
    status = FileAccess.objects.get(id=4)
    ser = FileAccessSerializer(status)
    print(ser.data)
