# Generated by Django 5.0.1 on 2024-02-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicapp', '0012_obj1'),
    ]

    operations = [
        migrations.CreateModel(
            name='obj2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj2content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='obj3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj3content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='obj4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj4content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='obj5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj5content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='obj6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj6content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='obj7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj7content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='pic1',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='templates/dynamic_page.html'),
        ),
    ]
