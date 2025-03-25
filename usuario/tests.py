import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from usuario.models import Usuario


@pytest.mark.django_db
def test_login_success():
    user = Usuario.objects.create_user(username='testuser', nome='Test User', password='password123')

    client = APIClient()
    url = reverse('api_login')
    data = {'username': 'testuser', 'password': 'password123'}
    response = client.post(url, data, format='json')

    assert response.status_code == 200
    assert 'token' in response.data

@pytest.mark.django_db
def test_login_failure():
    client = APIClient()
    url = reverse('api_login')
    data = {'username': 'wronguser', 'password': 'wrongpassword'}
    response = client.post(url, data, format='json')

    assert response.status_code == 400
    assert 'non_field_errors' in response.data

@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    url = reverse('usuario-list')
    data = {
        'username': 'newuser',
        'nome': 'New User',
        'password': 'password123'
    }
    response = client.post(url, data, format='json')

    # Verificar a resposta
    assert response.status_code == 201
    assert Usuario.objects.filter(username='newuser').exists()

@pytest.mark.django_db
def test_list_users():
    Usuario.objects.create_user(username='user1', nome='User One', password='password123')
    Usuario.objects.create_user(username='user2', nome='User Two', password='password123')

    user = Usuario.objects.get(username='user1')
    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse('usuario-list')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2
