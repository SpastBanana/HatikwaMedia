from django.db import models
import os
from uuid import uuid4


def song_file_path(instance, filename):
    # Get the name of the song from the instance
    song_name = instance.song_name

    # Generate a unique ID to use as the directory name
    directory_name = str(uuid4())

    # Construct the full path to the directory where the file will be uploaded
    directory_path = os.path.join('Songs', song_name)

    # Construct the full path to the file
    file_path = os.path.join(directory_path, filename)

    return file_path


class song_list(models.Model):
    topic_choises = (
        ('active', 'active'),
        ('inactive', 'inactive'),
        ('archive', 'archive'),
        ('folder', 'folder'),
    )
    song_name = models.CharField(max_length=200)
    page_topic = models.CharField(max_length=200, choices=topic_choises, default='active')
    guest_active = models.BooleanField(default=False)

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name_plural = "All songs"


class song_files(models.Model):
    type_choises = (
        ('main_sheet', 'main_sheet'),
        ('main_choreo', 'main_choreo'),
        ('main_audio', 'main_audio'),
        ('midi', 'midi'),
        ('other', 'other'),
    )
    song_name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200, choices=type_choises, default='other')
    song_file = models.FileField(upload_to=song_file_path)

    def __str__(self):
        return f"{self.song_name} - {self.item_type}"

    class Meta:
        verbose_name_plural = "Song files"