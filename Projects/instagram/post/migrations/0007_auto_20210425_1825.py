# Generated by Django 3.2 on 2021-04-25 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_profile_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='seen_num',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]
