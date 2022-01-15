# Generated by Django 4.0.1 on 2022-01-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_id_keygen_id_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keygen',
            name='dateTime',
        ),
        migrations.AddField(
            model_name='keygen',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='keygen',
            name='id_key',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
