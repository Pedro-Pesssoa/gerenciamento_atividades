"""
Pair programming - Pedro e Luma
"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from usuario.models import Usuario
from disciplinas.models import Disciplina, Atividade


# Testa a criação de uma nova disciplina
@pytest.mark.django_db
def test_create_disciplina():
    # Cria um usuário para autenticação
    user = Usuario.objects.create_user(username='testuser', nome='Test User', password='password123')

    client = APIClient()
    client.force_authenticate(user=user)  # Autentica o usuário

    url = reverse('disciplina-list')  # URL para criar disciplina
    data = {'nome': 'Matemática'}  # Dados da disciplina
    response = client.post(url, data, format='json')

    # Verifica se a disciplina foi criada com sucesso (status 201)
    assert response.status_code == 201
    assert Disciplina.objects.filter(nome='Matemática', usuario=user).exists()  # Confirma criação no banco


# Testa a criação de uma nova atividade associada a uma disciplina
@pytest.mark.django_db
def test_create_atividade():
    # Cria um usuário e uma disciplina para associação
    user = Usuario.objects.create_user(username='testuser', nome='Test User', password='password123')
    disciplina = Disciplina.objects.create(nome='Matemática', usuario=user)

    client = APIClient()
    client.force_authenticate(user=user)  # Autentica o usuário

    url = reverse('atividade-list', kwargs={'disciplina_pk': disciplina.pk})  # URL para criar atividade
    data = {
        'titulo': 'Trabalho de Matemática',
        'descricao': 'Resolver exercícios do capítulo 5',
        'status': 'N',
        'data_inicio': '2023-10-01',
        'data_entrega': '2023-10-15',
        'disciplina': disciplina.pk
    }
    response = client.post(url, data, format='json')

    # Verifica se a atividade foi criada com sucesso (status 201)
    assert response.status_code == 201
    assert Atividade.objects.filter(titulo='Trabalho de Matemática', disciplina=disciplina).exists()  # Confirma criação no banco
