# Generated by Django 4.0.1 on 2022-01-25 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_user_message_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='user',
            new_name='host',
        ),
    ]
