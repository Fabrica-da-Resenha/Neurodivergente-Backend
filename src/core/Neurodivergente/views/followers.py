from rest_framework import generics
from core.Neurodivergente.models import Follower
from core.Neurodivergente.serializers import followerSerializer
from django.contrib.auth.models import User

class FollowCreateView(generics.CreateAPIView):
    serializer_class = followerSerializer
    queryset = Follower.objects.all()

    def 