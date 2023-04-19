from django.db import models


class song_list(models.Model):
    song_name = models.CharField(max_length=200)

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name_plural = "All songs"


class song_sheetfiles(models.Model):
    song_name = models.CharField(max_length=200)
    main_item = models.BooleanField()
    song_file = models.FileField(upload_to=f'Songs/{song_name}')

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name_plural = "Sheets"


class song_soundfiles(models.Model):
    song_name = models.CharField(max_length=200)
    main_item = models.BooleanField()
    song_file = models.FileField(upload_to=f'Songs/{song_name}')

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name_plural = "Media (sounds & mp3)"


class song_mediafiles(models.Model):
    song_name = models.CharField(max_length=200)
    main_item = models.BooleanField()
    song_file = models.FileField(upload_to=f'Songs/{song_name}')

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name_plural = "Media (foto's and video's)"


class song_otherfiles(models.Model):
    song_name = models.CharField(max_length=200)
    song_file = models.FileField(upload_to=f'Songs/{song_name}')

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name_plural = "Other song files"