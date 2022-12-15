from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from drive_backend.users.api.views import UserViewSet
from drive_backend.file_system.api.views import FileViewSet, FolderViewSet, FilesandFolders

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register('files', FileViewSet)
router.register('folders', FolderViewSet)
router.register('utility/get_entities', FilesandFolders, basename='get_entities')

app_name = "api"
urlpatterns = router.urls
