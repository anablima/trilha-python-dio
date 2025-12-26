from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import TemplateView

# Rotas raiz do projeto: admin, login/logout, home e inclusão do app `cards`.
urlpatterns = [
    path("admin/", admin.site.urls),
    # Autenticação padrão do Django (views de login/logout)
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Página inicial (template simples)
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    # Inclui URLs do app de cartões com namespace
    path("cards/", include("cards.urls", namespace="cards")),
]
