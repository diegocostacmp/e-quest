
from django.urls import path, include
from apps.core import views
from .crud_views import (
    discipline_create, discipline_list,
    discipline_update, discipline_delete
    )
from .views import(
    login, sign_up,
    logout
)


app_name='core'

urlpatterns = [

    # signin and signup
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign-up'),
    path('logout/', views.logout, name='logout'),

    # DisciplineDetail
    path('create/', discipline_create, name='discipline-create'),
    path('list/', discipline_list, name='discipline-list'),
    path('update/', discipline_update, name='discipline-update'),
    path('delete/', discipline_delete, name='discipline-delete'),

    path('discipline/aluno/<uuid:uid_aluno>/add/', views.discipline_add_aluno, name='discipline_add_aluno'),
]
