"""
Pair programming - Pedro e Íris
"""
from rest_framework import viewsets, permissions
from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar operações CRUD de usuários.
    """

    #Retorna todos os objetos do modelo Usuario.
    queryset = Usuario.objects.all()

    #efine o serializador usado para serializar/desserializar dados.
    serializer_class = UsuarioSerializer

    #Permissões padrão aplicadas a todas as ações, exceto 'create'.
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        """
        Sobrescreve as permissões para permitir que qualquer usuário
        crie novos registros (ação 'create'). Para outras ações, 
        exige autenticação.
        """
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()
