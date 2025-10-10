from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationAPITest(APITestCase):
    """
    Suite de testes para o endpoint de registro de usuário.
    """

    def setUp(self):
        """
        Configuração inicial para os testes.
        self.url será o endereço do nosso endpoint: /api/register/
        """
        self.url = reverse('api-register') # Usa o 'name' da URL para evitar hardcoding
        self.valid_payload = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'strongpassword123'
        }

    def test_pode_criar_usuario_com_dados_validos(self):
        """
        Testa o "caminho feliz": garante que um usuário pode ser criado com sucesso.
        """
        # 1. Faz uma requisição POST para a nossa URL com os dados válidos
        response = self.client.post(self.url, self.valid_payload, format='json')

        # 2. Verifica se a resposta da API foi '201 CREATED'
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 3. Verifica se o usuário foi realmente criado no banco de dados
        self.assertEqual(User.objects.count(), 1)
        
        # 4. Verifica se os dados do usuário criado estão corretos
        created_user = User.objects.get()
        self.assertEqual(created_user.username, 'testuser')
        self.assertEqual(created_user.email, 'test@example.com')

    def test_nao_pode_criar_usuario_com_username_duplicado(self):
        """
        Testa o caso de erro: tenta criar um usuário com um username que já existe.
        """
        # Primeiro, criamos um usuário para que o username já exista
        User.objects.create_user(username='testuser', email='outro@email.com', password='pwd')
        
        # Agora, tentamos criar outro usuário com o mesmo username via API
        response = self.client.post(self.url, self.valid_payload, format='json')

        # Verifica se a API retornou '400 BAD REQUEST'
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Garante que nenhum novo usuário foi criado (ainda temos apenas 1)
        self.assertEqual(User.objects.count(), 1)
        
        # Verifica se a mensagem de erro está correta na resposta JSON
        self.assertIn('username', response.data)

    def test_nao_pode_criar_usuario_sem_password(self):
        """
        Testa o caso de erro: tenta criar um usuário sem a senha.
        """
        invalid_payload = {
            'username': 'anotheruser',
            'email': 'another@example.com',
            # 'password' está faltando
        }
        
        response = self.client.post(self.url, invalid_payload, format='json')

        # Verifica se a API retornou '400 BAD REQUEST'
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Garante que nenhum usuário foi criado
        self.assertEqual(User.objects.count(), 0)
        
        # Verifica se a mensagem de erro específica para o campo password foi retornada
        self.assertIn('password', response.data)
        self.assertEqual(str(response.data['password'][0]), 'Este campo é obrigatório.')