"""
Pair programming - Pedro e Íris
"""
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Usuario.
    """
    class Meta:
        #define model que será usada
        model = Usuario

        #define campos que serão usados
        fields = ['id', 'username', 'nome', 'password']

        #define que 'password' é somente para escrita e 'username' é obrigatório.
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True},
        }

    def create(self, validated_data):
        """
        Cria um novo usuário no banco de dados usando os dados validados.
        """
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            nome=validated_data['nome'],
            password=validated_data['password']
        )
        return user
