"""
Pair programming - Pedro e Luma
"""
from rest_framework import serializers
from .models import Disciplina, Atividade


class DisciplinaSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Disciplina.
    """
    class Meta:
        #Define model que será usada
        model = Disciplina

        #Define campos que serão usados
        fields = ['id', 'nome', 'usuario']

        #Define que o campo 'usuario' não pode ser alterado diretamente.
        read_only_fields = ['usuario']


class AtividadeSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Atividade.
    """
    class Meta:
        #Define model que será usada
        model = Atividade

        #Define campos que serão usados
        fields = ['id', 'titulo', 'descricao', 'status',
                  'data_inicio', 'data_entrega', 'disciplina']

    def validate_disciplina(self, value):
        """
        Garante que a disciplina selecionada pertença ao usuário autenticado.
        """
        if value.usuario != self.context['request'].user:
            raise serializers.ValidationError(
                "Você não tem permissão para associar esta atividade à disciplina selecionada.")
        return value
