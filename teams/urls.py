from teams import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('list_players/', views.list_players, name='list_players'),
    path('create_player/', views.create_player, name='create_player'),
]