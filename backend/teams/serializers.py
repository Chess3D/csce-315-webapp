from rest_framework import serializers
from .models import TeamMembers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    Team_Members = serializers.RelatedField(many=True)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'captain')