# Generated by Django 4.1.7 on 2023-04-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song_list',
            name='page_topic',
            field=models.CharField(choices=[('active', 'active'), ('archive', 'archive'), ('folder', 'folder')], default='active', max_length=200),
        ),
    ]