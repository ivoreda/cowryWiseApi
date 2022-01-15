# Generated by Django 4.0.1 on 2022-01-15 04:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyGen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
