"""
Pair programming - Pedro e Luma
"""
from rest_framework import viewsets, permissions
from .models import Atividade, Disciplina
from .serializers import AtividadeSerializer, DisciplinaSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar operações CRUD de disciplinas.
    """
    #Serializador usado para serializar/desserializar dados de Disciplina.
    serializer_class = DisciplinaSerializer

    #Exige que o usuário esteja autenticado para acessar as ações.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #Retorna disciplinas associadas ao usuário autenticado.
        return Disciplina.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        #Salva a disciplina com o usuário autenticado como proprietário.
        serializer.save(usuario=self.request.user)


class AtividadeViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar operações CRUD de atividades.
    """
    #Serializador usado para serializar/desserializar dados de Atividade.
    serializer_class = AtividadeSerializer

    #Exige que o usuário esteja autenticado para acessar as ações.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #Retorna atividades associadas às disciplinas do usuário autenticado.
        return Atividade.objects.filter(disciplina__usuario=self.request.user)

    def perform_create(self, serializer):
        #Salva a atividade com base nos dados fornecidos.
        serializer.save()
