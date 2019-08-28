from django.urls import path
from .views import (
    game_list, game_discipline_book,
    game_create, quiz_book_list, 
    game_await, students_online, game_await_aluno, 
    next_question, game_init, painel_quiz_aluno, quiz_book_list_aluno
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
    path('game_init/<uuid:uuid_question>/', game_init, name='game_init'),

    path('game_book_list/<uuid:game_uuid>/<int:discipline_id>/aluno/', quiz_book_list_aluno, name='quiz_book_list_aluno'),
    path('game_await/<uuid:game_uuid>/<uuid:quiz_uuid>/aluno/', game_await_aluno, name='game_await_aluno'),
    # path('painel/<uuid:game_uuid>/aluno/', painel_quiz_aluno, name='painel_quiz_aluno'),
    # path('game_list_aluno', game_list_aluno, name='game_list_aluno'),
]
