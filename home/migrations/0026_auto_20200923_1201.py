# Generated by Django 3.1.1 on 2020-09-23 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20200923_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletingtask',
            name='cherished_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 12, 1, 43, 754057), editable=False),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 12, 1, 33, 753579), editable=False),
        ),
    ]
