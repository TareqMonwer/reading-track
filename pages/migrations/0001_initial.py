# Generated by Django 3.0.2 on 2020-01-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Note title')),
                ('note_thumbnail', models.ImageField(default='thumbnail.png', upload_to='note_thumbnails', verbose_name='Note thumbnail')),
                ('note', models.TextField(verbose_name='Note description')),
                ('written_at', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]