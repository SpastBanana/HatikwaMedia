# Generated by Django 4.1.7 on 2023-04-19 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song_files',
            options={'verbose_name_plural': 'Song files'},
        ),
        migrations.AlterModelOptions(
            name='songs',
            options={'verbose_name_plural': 'Songs'},
        ),
    ]
