# Generated by Django 5.0.1 on 2024-02-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicapp', '0010_post1'),
    ]

    operations = [
        migrations.CreateModel(
            name='post2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p2content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='post3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p3content', models.TextField()),
            ],
        ),
    ]
