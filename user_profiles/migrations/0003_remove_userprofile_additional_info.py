# Generated by Django 5.0.7 on 2024-07-30 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_userprofile_github_userprofile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='additional_info',
        ),
    ]
