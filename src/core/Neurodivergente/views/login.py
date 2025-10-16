from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from core.Neurodivergente.serializers import UserLoginSerializer
from django.contrib.auth import authenticate
from core.Neurodivergente.models import Profile

@api_view(['POST'])
@permission_classes([AllowAny])
def login_usuario_api(request):
    """ ENDPOINT DA API PARA LOGAR O USUARIO """

    serializer = UserLoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)

        has_profile = Profile.objects.filter(user=user).exists()

        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'has_profile': has_profile
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response(
            {'detail': "Credenciais invalidas ou usuario inativo"},
            status=status.HTTP_401_UNAUTHORIZED
        )
            
    
            

        
