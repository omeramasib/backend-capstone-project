# Generated by Django 4.2.7 on 2023-11-27 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_menu_menuitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuItem',
            new_name='Menu',
        ),
    ]
