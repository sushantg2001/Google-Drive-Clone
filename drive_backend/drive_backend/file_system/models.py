from django.db import models

# Create your models here.
from drive_backend.users.models import User

class Folder(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Untitled')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','parent'], name='folder_parent_unique_constraint')
        ]

class File(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Untitled')
    file = models.FileField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','folder'], name='name_folder_unique_constraint')
        ]