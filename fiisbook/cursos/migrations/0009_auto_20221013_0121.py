# Generated by Django 2.0.9 on 2022-10-13 01:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_auto_20220929_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 1, 21, 24, 303706, tzinfo=utc)),
        ),
    ]
