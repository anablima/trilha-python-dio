from django.urls import path

from . import views

# Namespace do app e rotas de autenticação simples.
app_name = "accounts"
urlpatterns = [
    # Exibe formulário de login e trata POST para autenticar
    path("login/", views.authenticate_user, name="login"),
    # Efetua logout e redireciona para a página de login
    path("logout/", views.logout_user, name="logout"),
]
