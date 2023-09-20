from django.db import models


class user_permissions(models.Model):
    Permission = models.TextField()

    class Meta:
        verbose_name_plural = "User permissions"
        permissions = (
            ('Admin', 'Admin'),
            ('SettingsManager', 'SettingsManager'),
            ('AddUser', 'AddUser'),
            ('DeleteUser', 'DeleteUser'),
            ('ManageUser', 'ManageUser'),
        )

    def __str__(self):
        return self.Permission


class music_permissions(models.Model):
    Permission = models.TextField()

    class Meta:
        verbose_name_plural = "Music permissions"
        permissions = (
            ('AddSong', 'AddSong'),
            ('DeleteSong', 'DeleteSong'),
            ('ManageSong', 'ManageSong'),
        )

    def __str__(self):
        return self.Permission


class media_permissions(models.Model):
    Permission = models.TextField()

    class Meta:
        verbose_name_plural = "Media permissions"
        permissions = (
            ('AddMedia', 'AddMedia'),
            ('DeleteMedia', 'DeleteMedia'),
            ('ManageMedia', 'ManageMedia'),
        )

    def __str__(self):
        return self.Permission