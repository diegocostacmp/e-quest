from django.urls import path
from .views import (
    quiz_list, quiz_create,
    quiz_edit, quiz_delete,

    question_list, question_book,
    question_create
    )

app_name='quiz'

urlpatterns = [
    # listar quizzes
    path('quiz_list/<uuid:discipline_uuid>/', quiz_list, name='quiz_list'),
    path('quiz_create/', quiz_create, name='quiz_create'),
    path('quiz_edit/', quiz_edit, name='quiz_edit'),
    path('quiz_delete/', quiz_delete, name='quiz_delete'),

    path('question_list/<uuid:quiz_uuid>/', question_list, name='question_list'),
    path('question_book/', question_book, name='question_book'),
    path('question_create/', question_create, name='question_create')
]