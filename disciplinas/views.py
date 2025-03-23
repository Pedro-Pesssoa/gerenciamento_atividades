from rest_framework import viewsets, permissions
from .models import Atividade, Disciplina
from .serializers import AtividadeSerializer, DisciplinaSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Disciplina.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class AtividadeViewSet(viewsets.ModelViewSet):
    serializer_class = AtividadeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Atividade.objects.filter(disciplina__usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
