from django.urls import path
from .views import (
    game_list
)


app_name='game'

urlpatterns = [
    path('game_list', game_list, name='game_list')
]
