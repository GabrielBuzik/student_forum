# Generated by Django 2.2.9 on 2023-04-27 12:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussions', '0007_auto_20230427_0918'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vaccancy',
            new_name='Vacancy',
        ),
    ]
