from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Player(models.Model):

    username = models.CharField("Name", max_length=60)
    tournament = models.IntegerField("Tournament", default=-1)
    team = models.IntegerField("Team", default=-1)

def __str__(self):
        return self.username