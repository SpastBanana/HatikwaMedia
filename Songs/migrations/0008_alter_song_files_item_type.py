# Generated by Django 4.0 on 2024-01-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0007_song_files_delete_song_mediafiles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song_files',
            name='item_type',
            field=models.CharField(choices=[('main_sheet', 'main_sheet'), ('main_choreo', 'main_choreo'), ('main_audio', 'main_audio'), ('midi', 'midi'), ('other', 'other')], default='other', max_length=200),
        ),
    ]