# Generated by Django 3.2.4 on 2021-06-06 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeFeed', '0002_auto_20210606_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
    ]
