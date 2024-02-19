from django.contrib import admin
from .models import Team, Player


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'is_goalkeeper', 'team')


# Register your models here.
