# Generated by Django 5.1 on 2024-08-21 09:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_userprofileinfo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileInfo',
            new_name='UserProfileModel',
        ),
    ]
