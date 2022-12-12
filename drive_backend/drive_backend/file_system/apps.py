from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FileSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "drive_backend.file_system"
    verbose_name = _("File System")

    def ready(self):
        try:
            import drive_backend.file_system.signals  # noqa F401
        except ImportError:
            pass
