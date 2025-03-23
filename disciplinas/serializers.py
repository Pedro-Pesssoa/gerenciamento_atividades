from rest_framework import serializers
from .models import Disciplina, Atividade


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'usuario']
        read_only_fields = ['usuario']


class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'titulo', 'descricao', 'status',
                  'data_inicio', 'data_entrega', 'disciplina']

    def validate_disciplina(self, value):
        if value.usuario != self.context['request'].user:
            raise serializers.ValidationError(
                "Você não tem permissão para associar esta atividade à disciplina selecionada.")
        return value
