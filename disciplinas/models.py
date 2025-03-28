"""
Pair programming - Pedro e Luma
"""
from django.db import models
from usuario.models import Usuario


class Disciplina(models.Model):
    """
    Modelo que representa uma disciplina no sistema.
    """
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='disciplinas'
    )

    def __str__(self):
        """
        Retorna o nome da disciplina como representação em string.
        """
        return '${self.nome}'


class Atividade(models.Model):
    """
    Modelo que representa uma atividade vinculada a uma disciplina.
    """
    STATUS_CHOICES = [
        ('N', 'Não Iniciado'),
        ('P', 'Em Progresso'),
        ('C', 'Concluído'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='N'
    )
    data_inicio = models.DateField()
    data_entrega = models.DateField()
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='atividades'
    )

    def __str__(self):
        """
        Retorna o titulo  da atividade como representação em string.
        """
        return '${self.titulo}'
