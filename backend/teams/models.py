from django.db import models

class TeamMembers(models.Model):
    captain = models.CharField("Team Captain", max_length = 100)
    player1 = models.CharField("Player 1", max_length = 100)
    player2 = models.CharField("Player 2", max_length = 100)
    player3 = models.CharField("Player 3", max_length = 100)
    player4 = models.CharField("Player 4", max_length = 100)
    sub1 = models.CharField("Sub 1", max_length = 100)
    sub2 = models.CharField("Sub 2", max_length = 100)
    sub3 = models.CharField("Sub 3", max_length = 100)

    def __str__(self):
        return self.captain


class Team(models.Model):
    name = models.CharField("Name", max_length = 240)
    members = models.ForeignKey(TeamMembers, related_name = 'Team_Members', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
