# Generated by Django 3.1 on 2020-09-03 15:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_auto_20200903_1103"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playlist",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 9, 3, 15, 26, 58, 750812),
                editable=False,
            ),
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.URLField(max_length=128)),
                ("description", models.CharField(max_length=124)),
                ("check_relevance", models.BooleanField(default=False)),
                (
                    "playlist",
                    models.ForeignKey(
                        default="",
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.playlist",
                    ),
                ),
            ],
        ),
    ]
