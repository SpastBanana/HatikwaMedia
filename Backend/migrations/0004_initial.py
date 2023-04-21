# Generated by Django 4.1.7 on 2023-04-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Backend', '0003_delete_song_files_delete_songs'),
    ]

    operations = [
        migrations.CreateModel(
            name='member_invites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Outgoing invites',
            },
        ),
    ]