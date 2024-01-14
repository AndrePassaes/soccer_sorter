from django.shortcuts import render
from .models import Player, Team
from django.http import JsonResponse

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
    
