# Generated by Django 4.1.2 on 2022-11-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0005_alter_message_coordinate_x_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='keyboard_type',
            field=models.CharField(choices=[('RKB', 'Reply Keyboard'), ('IKB', 'Inline Keyboard')], default='RKB', max_length=3),
        ),
    ]
