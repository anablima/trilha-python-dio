from django.urls import path

from . import views

# Namespace do app e rotas de formulário/agradecimento/criação.
app_name = "contacts"
urlpatterns = [
    # Formulário para capturar nome
    path("", views.get_name, name="get_name"),
    # Página de agradecimento com parâmetro de nome
    path("thanks/<str:name>", views.thanks, name="thanks"),
    # Criação de contato (requer permissão)
    path("create/", views.create, name="create"),
]
