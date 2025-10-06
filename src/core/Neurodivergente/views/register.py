from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from core.Neurodivergente.serializers import UserCreateserializer



@api_view(['POST']) # O decorator @api_view define quais métodos HTTP esta view aceita.
@permission_classes([AllowAny]) # @permission_classes diz que qualquer um (mesmo não logado) pode acessar esta view.
def criar_usuario_api(request):
    """ Endpoint da API para criar um novo usuário. """

    serializer = UserCreateserializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        
        response_data = {
            'message': 'Usuário criado com sucesso!',
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    