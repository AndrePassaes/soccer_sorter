from django.shortcuts import render
from .models import Player, Team
from django.http import JsonResponse

import random

def index(request):
    players = Player.objects.all()
    teams = Team.objects.all()
    context = {
        'players': players,
        'teams': teams
    }
    return render(request, 'teams/index.html', context)

def list_players(request):
    players = list(Player.objects.values())
    return JsonResponse(players, safe=False)

def create_player(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        grade = request.POST.get('grade')
        is_goalkeeper = request.POST.get('is_goalkeeper')
        team = request.POST.get('team')
        player = Player(name=name, grade=grade, is_goalkeeper=is_goalkeeper, team=team)
        player.save()
        return JsonResponse({'message': 'Player created successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})

def sort_players(players, max_per_team):
    #Separate goalkeepers and oufield players
    gks = [p for p in players if p.is_goalkeeper]
    outfielders = [p for p in players if not p.is_goalkeeper]
    
    #Randomly sort if no grades are provided
    if all(p.grade == 0 for p in players):
        random.shuffle(gks)
        random.shuffle(outfielders)
    else:
        #Sort by grade
        gks.sort(key=lambda x: x.grade, reverse=True)
        players.sort(key=lambda x: x.grade, reverse=True)
    
    #Create teams
    teams = {'Team 1':[], 'Team 2': []}
    #Distribute players between teams
    for i, player in enumerate(players):
        teams['Team 1' if i % 2 == 0 else 'Team 2'].append(player)
    
    return teams