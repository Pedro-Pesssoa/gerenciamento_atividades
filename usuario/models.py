"""
Pair programming - Pedro e Íris
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """
    Modelo personalizado de Usuário que estende AbstractUser.
    """
    nome = models.CharField(max_length=150)

    #identificador único para login
    USERNAME_FIELD = 'username'
    #campos obrigatórios ao criar um usuário
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        """
        Retorna o nome do usuário como representação em string.
        """
        return '${self.nome}'
