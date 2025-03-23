from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    # Administração
    path('admin/', admin.site.urls),

    # Documentação da API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Autenticação
    path('api/login/', obtain_auth_token, name='api_login'),

    # Rotas da app usuario
    path('api/', include('usuario.urls')),
    path('api/disciplinas/', include('disciplinas.urls')),
]
