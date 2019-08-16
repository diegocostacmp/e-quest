from django.urls import path
from .views import (
    game_list, game_discipline_book,
    game_create, quiz_book_list
)


app_name='game'

urlpatterns = [
    path('game_list', game_list, name='game_list'),
    path('quiz_book_list/<uuid:discipline_uuid>/', quiz_book_list, name='quiz_book_list'),
    path('game_discipline_book', game_discipline_book, name='game_discipline_book'),
    path('game_create/<uuid:discipline_uuid>/', game_create, name='game_create')
]
