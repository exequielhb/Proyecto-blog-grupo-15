# Generated by Django 3.1.13 on 2021-12-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0004_auto_20211207_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
