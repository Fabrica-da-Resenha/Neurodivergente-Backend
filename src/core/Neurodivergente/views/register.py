from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from core.Neurodivergente.serializers import UserCreateserializer



@api_view(['POST'])
@permission_classes([AllowAny])
def criar_usuario_api(request):
    """ Endpoint da API para criar um novo usuário. """

    serializer = UserCreateserializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save(user=request.user)
        
        response_data = {
            'message': 'Usuário criado com sucesso!',
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    