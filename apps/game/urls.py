from django.urls import path
from .views import (
    game_list, game_discipline_book,
    quizzes_discipline
)


app_name='game'

urlpatterns = [
    path('game_list', game_list, name='game_list'),
    path('game_discipline_book', game_discipline_book, name='game_discipline_book'),
    path('quizzes_discipline', quizzes_discipline, name='quizzes_discipline')
]
