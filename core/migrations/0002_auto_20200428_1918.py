# Generated by Django 2.2.10 on 2020-04-28 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaboration',
            name='image',
        ),
        migrations.RemoveField(
            model_name='collaborationrequest',
            name='image',
        ),
    ]