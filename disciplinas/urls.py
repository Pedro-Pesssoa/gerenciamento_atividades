from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DisciplinaViewSet, AtividadeViewSet

router = DefaultRouter()
router.register(r'disciplinas', DisciplinaViewSet, basename='disciplina')

urlpatterns = [
    path('', include(router.urls)),
    path('disciplinas/<int:disciplina_pk>/atividades/', AtividadeViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='atividade-list'),
    
    path('disciplinas/<int:disciplina_pk>/atividades/<int:pk>/', AtividadeViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='atividade-detail'),
]