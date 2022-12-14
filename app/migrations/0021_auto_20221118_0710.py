# Generated by Django 3.2 on 2022-11-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_paper_link_paper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract_eng',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract_thai',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='keyword',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='paper',
            name='link_paper',
            field=models.URLField(blank=True),
        ),
    ]
