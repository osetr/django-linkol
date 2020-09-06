# Generated by Django 3.1 on 2020-09-06 13:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_auto_20200904_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 6, 13, 0, 55, 483207), editable=False),
        ),
        migrations.CreateModel(
            name='Evaluating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0, editable=False)),
                ('dislikes', models.IntegerField(default=0, editable=False)),
                ('author', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('playlist', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='home.playlist')),
            ],
        ),
    ]
