# Generated by Django 3.1 on 2020-09-03 10:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_auto_20200903_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 3, 10, 59, 44, 790308), editable=False),
        ),
    ]
