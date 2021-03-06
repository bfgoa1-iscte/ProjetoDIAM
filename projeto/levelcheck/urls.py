from django.urls import include, path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

# (. significa que importa views da mesma directoria)

app_name = 'levelcheck'
urlpatterns = [
    path('', views.login_form, name='login_form'),
    path('logout', views.logout, name='logout'),
    path('createacc', views.create_acc, name='create_acc'),
    path('index', views.index, name='index'),
    path('allgames', views.all_games, name='all_games'),
    path('allcharacters', views.all_characters, name='all_characters'),
    path('allreviews', views.all_reviews, name='all_reviews'),
    path('allusers', views.all_users, name='all_users'),
    path('creategame', views.create_game, name='create_game'),
    path('deletegame/<str:title>', views.delete_game, name='delete_game'),
    path('creategenre', views.create_genre, name='create_genre'),
    path('review/vote/<int:review_id>/<str:type>', views.review_feedback_vote, name='review_feedback_vote'),
    path('stats/<str:title>/<str:type>', views.user_games_stats, name='user_games_stats'),
    path('follow/<str:owner_id>', views.follower_followed, name='follower_followed'),
    path('favourite/<str:title>/<str:name>', views.user_characters_favourites, name='user_characters_favourites'),
    path('createcharacter', views.create_character, name='create_character'),
    path('createarticle', views.create_article, name='create_article'),
    path('deletecharacter/<str:title>/<str:name>', views.delete_character, name='delete_character'),
    path('createreview/<str:title>', views.create_review, name='create_review'),
    path('deletereview/<str:game_id>', views.delete_review, name='delete_review'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('editprofile/<int:id>', views.edit_profile, name='edit_profile'),
    path('<int:id>', views.user_detail, name='user_detail'),
    path('<str:title>', views.game_detail, name='game_detail'),
    path('<str:title>/<str:name>', views.character_detail, name='character_detail'),
    path('review/<str:username>/<int:id>', views.review_detail, name='review_detail'),
]
