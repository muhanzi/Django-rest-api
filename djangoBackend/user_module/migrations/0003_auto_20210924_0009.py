# Generated by Django 3.1.2 on 2021-09-23 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0002_auto_20210924_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 0, 9, 6, 514538)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 0, 9, 6, 514538)),
        ),
        migrations.AlterField(
            model_name='recrutingagency',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 0, 9, 6, 513541)),
        ),
        migrations.AlterField(
            model_name='recrutingagency',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 0, 9, 6, 513541)),
        ),
        migrations.AlterField(
            model_name='supersite',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 0, 9, 6, 514538)),
        ),
        migrations.AlterField(
            model_name='supersite',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 0, 9, 6, 514538)),
        ),
    ]