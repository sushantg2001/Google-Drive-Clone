from drive_backend.file_system.models import File, Folder
from drive_backend.users.models import User

def run():
    # File.objects.all().delete()
    # Folder.objects.all().delete()
    User.objects.delete(username='test_user')
