# Generated by Django 4.2.2 on 2023-06-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('describtions', models.TextField()),
                ('type', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='media/')),
                ('thumbnails', models.ImageField(upload_to='media/')),
                ('sample_video', models.FileField(upload_to='media/')),
                ('size', models.IntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]