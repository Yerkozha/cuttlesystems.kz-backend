# Generated by Django 4.1.2 on 2023-01-17 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0013_alter_variant_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='error_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='error_message_bot', to='bots.message'),
        ),
    ]
