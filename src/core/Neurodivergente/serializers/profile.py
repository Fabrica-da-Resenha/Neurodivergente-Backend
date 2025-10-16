from rest_framework import serializers
from core.Neurodivergente.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = '__all__'
        
        read_only_fields = ["user"]
