from django.db import models
from games.models import Games


class Level(models.Model):
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE, default=1)
    level_description = models.TextField()
    video_name = models.CharField(max_length= 20)
    video_description = models.TextField()
    level_number = models.PositiveSmallIntegerField()
    level_scores = models.PositiveSmallIntegerField()

    def __self__(self):
        return f"{self.level_number}"
