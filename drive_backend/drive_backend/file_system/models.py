from django.db import models

# Create your models here.
from drive_backend.users.models import User

class Folder(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Untitled')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through='FolderAccess', related_name='folders')

    @property
    def path(self):
        if self.id == 0:
            return '/root'
        current_path = f'{self.parent.path}/{self.name}'
        return current_path

    class Meta:
        unique_together = ['name', 'parent']

    def __str__(self) -> str:
        if self.id == 0:
            return 'root folder'
        else:
            return f'{self.name}, {self.id}, {self.owner.username}'

class File(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Untitled')
    file = models.FileField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    parent = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='files', through='FileAccess')
    size = models.PositiveSmallIntegerField(editable=False, null=True)

    @property
    def path(self):
        if self.id == 0:
            return '/root'
        parent_path = self.parent.path
        current_path = f'{parent_path}/{self.name}'
        return current_path

    class Meta:
        unique_together = ['name', 'parent']

    def __str__(self):
        return f'{self.name}, {self.id}, {self.owner.username}'

class FileAccess(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='access')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('viewer', 'viewer'), ('editor', 'editor')], default='viewer')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        unique_together = ['user', 'file']

class FolderAccess(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='access')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('viewer', 'viewer'), ('editor', 'editor')], default='viewer')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        unique_together = ['user', 'folder']