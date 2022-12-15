from drive_backend.users.api.serializers import UserDetailSerializer
from drive_backend.users.models import User

def run():
    user = User.objects.get(username = 'admin')
    user_ser = UserDetailSerializer(user)
    print(user_ser.data)
