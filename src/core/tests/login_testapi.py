from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class UserAuthenticateAPITest(APITestCase):
    """ Teste de casos para api de autentificação (LOGIN) """
    def setUp(self):
        """
        Configuração inicial para os testes.
        Este método é executado antes de cada teste.
        """
        # 1. Crie um usuário de teste no banco de dados para poder fazer o login.
        self.username = 'testuser'
        self.password = 'strongpassword123'
        self.user = User.objects.create_user(
            username=self.username,
            email='test@example.com',
            password=self.password
        )

        # 2. Defina a URL do endpoint de login.
        self.url = reverse('api-login')

        # 3. Defina o payload com os dados corretos para o login.
        self.valid_payload = {
            'username': self.username,
            'password': self.password
        }

    def test_login_with_valid_credentials(self):
        """
        Garante que um usuário consegue se autenticar com credenciais válidas.
        """
        # 1. Faz uma requisição POST para a URL de login com dados válidos.
        response = self.client.post(self.url, self.valid_payload, format='json')

        # 2. Verifica se a resposta da API foi '200 OK'.
        #    Esta é a resposta correta para um login bem-sucedido.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 3. (Opcional, mas recomendado) Verifica se a resposta contém os tokens.
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_with_invalid_credentials(self):
        """
        Garante que um usuário não consegue se autenticar com uma senha incorreta.
        """
        # 1. Cria um payload com a senha errada.
        invalid_payload = {
            'username': self.username,
            'password': 'wrongpassword'
        }
        
        # 2. Faz a requisição POST com os dados inválidos.
        response = self.client.post(self.url, invalid_payload, format='json')

        # 3. Verifica se a resposta foi '401 UNAUTHORIZED'.
        #    (Dependendo da implementação, também poderia ser 400 BAD REQUEST).
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)