from django.urls import path
from .crud_views import (
    quiz_list, quiz_create,
    quiz_update, quiz_delete
    )
from .views import(
    question_list, question_book,
    question_create, question_delete,
    question_book_preview
)

app_name='quiz'

urlpatterns = [
    path('list/<uuid:discipline_uuid>/', quiz_list, name='quiz-list'),
    path('create/', quiz_create, name='quiz-create'),
    path('update/', quiz_update, name='quiz-update'),
    path('delete/', quiz_delete, name='quiz-delete'),

    path('question_list/<uuid:quiz_uuid>/', question_list, name='question_list'),
    path('question_book/', question_book, name='question_book'),
    path('question_book_preview/', question_book_preview, name='question_book_preview'),
    path('question_create/', question_create, name='question_create'),
    path('question_delete/', question_delete, name='question_delete')
]