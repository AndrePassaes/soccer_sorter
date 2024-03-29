"""
URL configuration for soccer_sorter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teams import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', views.list_players, name='list_players'),
    path('index/', views.index, name='index'),    
    path('create_player/', views.create_player, name='create_player'),
    path('sort_players/', views.sort_players, name='sort_players'),
    #add paths for other views
]
