from django.db.models.signals import post_save, pre_save
from .models import File, Folder, FileAccess, FolderAccess
from drive_backend.users.models import User
from django.dispatch import receiver

admin = User.objects.get(username = 'admin')
root = Folder.objects.get(pk=0)

@receiver(pre_save, sender=File)
def file_size(sender, instance, *args, **kwargs):
    try:
        instance.size = instance.file.size
        File.objects.get(id=instance.id)
    except File.DoesNotExist:
        pass

@receiver(pre_save, sender=File)
def file_ext(sender, instance, *args, **kwargs):
    try:
        instance.ext = instance.file.path.split('.')[1]
        prev = File.objects.get(id=instance.id)
    except File.DoesNotExist:
        pass

@receiver(post_save, sender=User)
def base_folder(sender, instance, created, *args, **kwawrgs):
    if created:
        Folder.objects.create(
            name= instance.username,
            owner = instance,
            parent = root
        )

@receiver(pre_save, sender=FileAccess)
def update_slug_file(sender, instance, *args, **kwargs):
    try:
        instance.slug = f'{instance.user.id}-{instance.file.id}'
    except FileAccess.DoesNotExist:
        pass

@receiver(pre_save, sender=FolderAccess)
def update_slug_folder(sender, instance, *args, **kwargs):
    try:
        instance.slug = f'{instance.user.id}-{instance.folder.id}'
    except FolderAccess.DoesNotExist:
        pass