# Generated by Django 4.0.3 on 2022-05-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelcheck', '0012_review_review_title'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('user', 'game'), name='user_game_review'),
        ),
    ]
