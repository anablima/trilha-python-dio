from django.urls import path

from . import views

# Mapeamento das rotas do app de enquetes.
app_name = "polls"
urlpatterns = [
    # Lista de perguntas
    path("", views.index, name="index"),
    # Detalhe da pergunta por ID
    path("<int:question_id>/", views.detail, name="detail"),
    # Página de resultados da pergunta
    path("<int:question_id>/results/", views.results, name="results"),
    # Submissão de voto para a pergunta
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
