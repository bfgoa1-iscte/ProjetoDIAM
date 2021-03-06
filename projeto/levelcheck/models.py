import django.utils.timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Genre(models.Model):
    genre = models.CharField(max_length=50, primary_key=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)


class Game(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='games/')
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    release = models.DateField('Release Date')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    pub_date = models.DateTimeField('Posted', default=timezone.now)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'game'], name='user_game_review')]


class ReviewFeedback(models.Model):
    FEEDBACK_OPTIONS = (('L', 'Like'), ('D', 'Dislike'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='feedback')
    type = models.CharField(max_length=1, choices=FEEDBACK_OPTIONS)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='feedback')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'review'], name='user_review_feedback')]


class Character(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    img = models.ImageField(upload_to='characters/')
    pub_date = models.DateTimeField('Posted', default=timezone.now)


class LevelUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, default="Prefer not")
    birthday = models.CharField(max_length=50)
    img_src = models.CharField(max_length=150)
    location = models.CharField(max_length=50, default="Earth")
    joined = models.DateField('Joined')
    bio = models.CharField(max_length=500, default="Your Bio!")

    def __str__(self):
        return self.user


class UserGames(models.Model):
    FEEDBACK_OPTIONS = (('P', 'Playing'), ('C', 'Completed'), ('H', 'Hold'), ('D', 'Dropped'), ('F', 'Plan-to-Play'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=FEEDBACK_OPTIONS)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'game'], name='user_game_stats')]


class UserCharacters(models.Model):
    FEEDBACK_OPTIONS = (('F', 'Favourite'), ('U', 'Unfavourite'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=FEEDBACK_OPTIONS)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'character', 'game'], name='user_character_favourites')]


class UserFollowers(models.Model):
    FEEDBACK_OPTIONS = (('F', 'Follow'), ('U', 'Unfollow'))
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    type = models.CharField(max_length=1, choices=FEEDBACK_OPTIONS)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['follower', 'followed'], name='follower_followed')]


class Article(models.Model):
    title = models.CharField(max_length=75, primary_key=True)
    link = models.CharField(max_length=150)
    img = models.ImageField(upload_to='news/')
    pub_date = models.DateTimeField('Posted', default=timezone.now)
