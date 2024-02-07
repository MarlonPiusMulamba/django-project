# Generated by Django 5.0.1 on 2024-02-05 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicapp', '0006_slogan'),
    ]

    operations = [
        migrations.CreateModel(
            name='pic1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='slogan_images/')),
            ],
        ),
    ]