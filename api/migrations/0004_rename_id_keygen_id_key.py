# Generated by Django 4.0.1 on 2022-01-15 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_keygen_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keygen',
            old_name='id',
            new_name='id_key',
        ),
    ]
