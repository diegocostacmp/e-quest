from django.urls import path
from .views import (
    game_list, game_discipline_book,
    game_create, quiz_book_list, 
    game_await, students_online,
    next_question, game_init
)


app_name='game'

urlpatterns = [
    path('game_list', game_list, name='game_list'),
    path('quiz_book_list/<uuid:discipline_uuid>/<uuid:game_uuid>/', quiz_book_list, name='quiz_book_list'),
    path('game_discipline_book', game_discipline_book, name='game_discipline_book'),
    path('game_create/<uuid:discipline_uuid>/', game_create, name='game_create'),
    path('game_await/<uuid:game_uuid>/<uuid:quiz_uuid>/', game_await, name='game_await'),


    path('students_online/', students_online, name='students_online'),
    path('next_question/', next_question, name='next_question'),
    path('game_init/<uuid:uuid_question>/', game_init, name='game_init')
]
