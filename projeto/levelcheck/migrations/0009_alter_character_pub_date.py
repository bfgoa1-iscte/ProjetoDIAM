# Generated by Django 4.0.3 on 2022-05-14 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('levelcheck', '0008_alter_character_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 14, 17, 17, 6, 369284, tzinfo=utc), verbose_name='Posted'),
        ),
    ]
