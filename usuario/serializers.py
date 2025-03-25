from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'nome', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True},
        }

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            nome=validated_data['nome'],
            password=validated_data['password']
        )
        return user
