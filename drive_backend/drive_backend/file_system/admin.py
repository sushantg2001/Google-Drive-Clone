from django.contrib import admin
from drive_backend.file_system.models import File, Folder, FileAccess, FolderAccess

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass

@admin.register(FileAccess)
class FileAccessAdmin(admin.ModelAdmin):
    pass

@admin.register(FolderAccess)
class FolderAccessAdmin(admin.ModelAdmin):
    pass