# Generated by Django 4.2 on 2024-05-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_profile_owner_profile_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
