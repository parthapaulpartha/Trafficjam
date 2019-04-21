# Generated by Django 2.1.2 on 2019-04-21 07:30

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Weather'},
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(default=None, on_delete='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 13, 30, 53, 732490)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.ForeignKey(default=None, on_delete='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postcreate',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 13, 30, 53, 730489)),
        ),
        migrations.AlterField(
            model_name='postcreate',
            name='name',
            field=models.ForeignKey(default=None, on_delete='', to=settings.AUTH_USER_MODEL),
        ),
    ]
