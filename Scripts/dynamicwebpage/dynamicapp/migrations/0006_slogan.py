# Generated by Django 5.0.1 on 2024-02-05 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicapp', '0005_remove_vision_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='slogan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slcontent', models.TextField()),
            ],
        ),
    ]
