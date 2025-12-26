from django.contrib import admin

from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem do admin
    list_display = ("number", "user", "network", "status", "created_at")
    # Filtros laterais para facilitar buscas
    list_filter = ("status", "network", "created_at")
    # Campos pesquisáveis (inclui lookup por nome de usuário)
    search_fields = ("user__username", "status")
