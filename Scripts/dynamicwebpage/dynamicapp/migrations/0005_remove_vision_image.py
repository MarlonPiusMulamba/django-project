# Generated by Django 5.0.1 on 2024-02-05 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicapp', '0004_vision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vision',
            name='image',
        ),
    ]