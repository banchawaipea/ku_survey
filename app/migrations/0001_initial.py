# Generated by Django 3.2 on 2022-11-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('abstract_thai', models.TextField()),
                ('abstract_eng', models.TextField()),
                ('upload_files', models.FileField(blank=True, null=True, upload_to='file')),
            ],
        ),
    ]
