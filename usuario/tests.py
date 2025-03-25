"""
Pair programming - Pedro e Íris
"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from usuario.models import Usuario


# Testa login bem-sucedido
@pytest.mark.django_db
def test_login_success():
    # Cria um usuário para teste
    user = Usuario.objects.create_user(username='testuser', nome='Test User', password='password123')

    client = APIClient()
    url = reverse('api_login')  # URL para login
    data = {'username': 'testuser', 'password': 'password123'}  # Dados válidos
    response = client.post(url, data, format='json')

    # Verifica se o login foi bem-sucedido (status 200) e retorna token
    assert response.status_code == 200
    assert 'token' in response.data


# Testa falha no login com credenciais inválidas
@pytest.mark.django_db
def test_login_failure():
    client = APIClient()
    url = reverse('api_login')  # URL para login
    data = {'username': 'wronguser', 'password': 'wrongpassword'}  # Dados inválidos
    response = client.post(url, data, format='json')

    # Verifica se o login falhou (status 400) e retorna erro específico
    assert response.status_code == 400
    assert 'non_field_errors' in response.data


# Testa criação de novo usuário
@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    url = reverse('usuario-list')  # URL para criar usuário
    data = {
        'username': 'newuser',
        'nome': 'New User',
        'password': 'password123'
    }
    response = client.post(url, data, format='json')

    # Verifica se o usuário foi criado com sucesso (status 201)
    assert response.status_code == 201
    assert Usuario.objects.filter(username='newuser').exists()  # Confirma que o usuário existe no banco


# Testa listagem de usuários autenticados
@pytest.mark.django_db
def test_list_users():
    # Cria dois usuários para teste
    Usuario.objects.create_user(username='user1', nome='User One', password='password123')
    Usuario.objects.create_user(username='user2', nome='User Two', password='password123')

    # Autentica o primeiro usuário
    user = Usuario.objects.get(username='user1')
    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse('usuario-list')  # URL para listar usuários
    response = client.get(url)

    # Verifica se a listagem foi bem-sucedida (status 200) e retorna todos os usuários
    assert response.status_code == 200
    assert len(response.data) == 2  # Confirma que há 2 usuários na resposta
