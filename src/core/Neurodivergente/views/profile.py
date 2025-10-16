from rest_framework.viewsets import ModelViewSet

from core.Neurodivergente.models import Profile
from core.Neurodivergente.serializers import ProfileSerializer

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer