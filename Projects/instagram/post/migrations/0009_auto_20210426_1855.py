# Generated by Django 3.2 on 2021-04-26 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_delete_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_date',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='update_date',
        ),
    ]
