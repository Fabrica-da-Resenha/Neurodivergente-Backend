from rest_framework import serializers
from core.Neurodivergente.models import Follower

class followerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ["user_followed"]