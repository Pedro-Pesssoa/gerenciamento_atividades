import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from usuario.models import Usuario
from disciplinas.models import Disciplina, Atividade


@pytest.mark.django_db
def test_create_disciplina():
    user = Usuario.objects.create_user(username='testuser', nome='Test User', password='password123')

    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse('disciplina-list')
    data = {'nome': 'Matemática'}
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert Disciplina.objects.filter(nome='Matemática', usuario=user).exists()

@pytest.mark.django_db
def test_create_atividade():
    user = Usuario.objects.create_user(username='testuser', nome='Test User', password='password123')
    disciplina = Disciplina.objects.create(nome='Matemática', usuario=user)

    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('atividade-list', kwargs={'disciplina_pk': disciplina.pk})
    data = {
        'titulo': 'Trabalho de Matemática',
        'descricao': 'Resolver exercícios do capítulo 5',
        'status': 'N',
        'data_inicio': '2023-10-01',
        'data_entrega': '2023-10-15',
        'disciplina': disciplina.pk
    }
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert Atividade.objects.filter(titulo='Trabalho de Matemática', disciplina=disciplina).exists()
