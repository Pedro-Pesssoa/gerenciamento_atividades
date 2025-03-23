from django.contrib import admin
from .models import Disciplina, Atividade


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario')
    list_filter = ('usuario',)
    search_fields = ('nome',)


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'status', 'data_inicio', 'data_entrega')
    list_filter = ('status', 'disciplina__nome')
    search_fields = ('titulo', 'descricao')
