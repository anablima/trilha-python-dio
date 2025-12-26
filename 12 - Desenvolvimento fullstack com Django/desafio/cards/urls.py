from django.urls import path

from . import views

# Namespace do app e mapeamento das rotas de cartões.
app_name = "cards"
urlpatterns = [
    # Solicitar novo cartão
    path("request-card/", views.request_card, name="request_card"),
    # Visualizar solicitações do usuário
    path("my-requests/", views.view_requests, name="view_requests"),
    # Detalhar uma solicitação específica
    path("request-details/<int:card_id>/", views.card_details, name="card_details"),
]
