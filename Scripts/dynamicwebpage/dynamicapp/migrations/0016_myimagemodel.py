# Generated by Django 5.0.2 on 2024-02-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicapp', '0015_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('prob', models.FloatField()),
                ('imagen', models.ImageField(upload_to='hongo_images/')),
            ],
        ),
    ]
