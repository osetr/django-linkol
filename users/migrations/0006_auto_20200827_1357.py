# Generated by Django 3.1 on 2020-08-27 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_auto_20200826_1732"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 27, 13, 57, 29, 706204),
                editable=False,
            ),
        ),
    ]
