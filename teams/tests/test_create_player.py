import pytest

from django.test import TestCase
from teams.models import Player, Team
from teams.views import create_player
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_create_player_with_all_required_fields():
    player = Player(name="Ananias", grade=5, is_goalkeeper=False)
    assert player.name == "Ananias"
    assert player.grade == 5
    assert player.is_goalkeeper == False

def test_create_player_with_only_required_fields():
    player = Player(name="Ananias")
    assert player.name == "Ananias"
    
def test_update_player_name():
    player = Player(name="Ananias", grade = 5, is_goalkeeper=False)
    player.name = "Epaminondas"
    assert player.name == "Epaminondas"