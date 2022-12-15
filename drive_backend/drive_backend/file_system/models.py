from django.db import models

# Create your models here.
from drive_backend.users.models import User

class Folder(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Untitled')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through='FolderAccess', related_name='folders', related_query_name='folder')

    @property
    def path(self):
        if self.id == 0:
            return '/root'
        current_path = f'{self.parent.path}/{self.name}'
        return current_path

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','parent'], name='folder_parent_unique_constraint')
        ]
    def __str__(self) -> str:
        if self.id == 0:
            return 'root folder'
        else:
            return f'{self.name}, {self.id}, {self.owner.username}'

class File(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Untitled')
    ext = models.CharField(editable=False, max_length=10, null=True)
    file = models.FileField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='files', related_query_name='file', through='FileAccess')
    size = models.PositiveSmallIntegerField(editable=False, null=True)

    @property
    def path(self):
        if self.id == 0:
            return '/root'
        parent_path = self.folder.path
        current_path = f'{parent_path}/{self.name}.{self.ext}'
        return current_path
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','folder'], name='name_folder_unique_constraint')
        ]
    def __str__(self):
        return f'{self.name}, {self.id}, {self.owner.username}'

class FileAccess(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, null=True, related_name='access')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, choices=[('viewer', 'viewer'), ('editor', 'editor')], default='viewer')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['file', 'user'], name='file_user_unique_constraint')
        ]


class FolderAccess(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, related_name='access')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, choices=[('viewer', 'viewer'), ('editor', 'editor')], default='viewer')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['folder', 'user'], name='folder_user_unique_constraint')
        ]