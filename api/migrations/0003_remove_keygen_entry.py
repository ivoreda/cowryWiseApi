# Generated by Django 4.0.1 on 2022-01-15 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_keygen_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keygen',
            name='entry',
        ),
    ]
