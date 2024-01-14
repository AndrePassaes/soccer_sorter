from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField(default=0, choices=[
        (i, i) for i in range(6)])
    is_goalkeeper = models.BooleanField(default=False)
    team = models.ForeignKey(
        'Team',
        related_name='players',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, default='Team')
    
    def __str__(self):
        return self.name
    
