# Generated by Django 4.0.3 on 2022-05-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelcheck', '0011_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_title',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
    ]
