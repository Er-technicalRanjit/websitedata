# Generated by Django 2.2.2 on 2019-07-21 01:50

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('websitedata', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('london', django.db.models.manager.Manager()),
            ],
        ),
    ]
