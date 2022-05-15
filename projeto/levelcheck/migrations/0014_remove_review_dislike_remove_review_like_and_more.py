# Generated by Django 4.0.3 on 2022-05-14 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('levelcheck', '0013_review_user_game_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='review',
            name='like',
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Posted'),
        ),
        migrations.CreateModel(
            name='ReviewFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('L', 'Like'), ('D', 'Dislike')], max_length=1)),
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='levelcheck.review')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='feedback', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]