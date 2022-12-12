from drive_backend.users.api.serializers import UserSerializerExtra
from drive_backend.users.models import User

def run():
    user = User.objects.get(username = 'admin')
    user_ser = UserSerializerExtra(user)
    print(user_ser.data)
