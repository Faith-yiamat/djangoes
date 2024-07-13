from django.db import models
from games.models import Games

class User(models.Model):

    full_name = models.CharField(max_length= 40)
    email = models.EmailField()
    user_name = models.CharField(max_length= 40)
    password = models.CharField(max_length= 20)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE)

    
