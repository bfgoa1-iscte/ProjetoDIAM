# Generated by Django 4.0.3 on 2022-05-15 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('levelcheck', '0021_article_delete_discussion'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('F', 'Follow'), ('U', 'Unfollow')], max_length=1)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='userfollowers',
            constraint=models.UniqueConstraint(fields=('follower', 'followed'), name='follower_followed'),
        ),
    ]
