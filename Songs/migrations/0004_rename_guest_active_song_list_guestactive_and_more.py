# Generated by Django 4.1.7 on 2023-05-16 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0003_song_list_guest_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song_list',
            old_name='guest_active',
            new_name='guestactive',
        ),
        migrations.RenameField(
            model_name='song_list',
            old_name='page_topic',
            new_name='pagetopic',
        ),
        migrations.RenameField(
            model_name='song_list',
            old_name='song_name',
            new_name='songname',
        ),
    ]
