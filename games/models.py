from django.db import models



# Create your models here.

class Games(models.Model):
    game_id = models.PositiveSmallIntegerField(primary_key=True)
    game_name = models.CharField(max_length= 40)
    game_levels = models.PositiveSmallIntegerField()
    game_description = models.TextField()



    def __self__(self):
        return f"{self.game_name}"

   