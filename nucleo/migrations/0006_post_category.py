# Generated by Django 3.1.13 on 2021-12-08 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=1, max_length=255),
        ),
    ]