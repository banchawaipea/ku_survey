# Generated by Django 3.2 on 2022-11-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(height_field=28, null=True, upload_to='avatar', width_field=28),
        ),
    ]
