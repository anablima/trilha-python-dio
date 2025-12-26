from config.admin import admin_site
from django.urls import include, path

# Rotas raiz: admin customizado e inclusão dos apps.
urlpatterns = [
    path("admin/", admin_site.urls),
    # Enquetes
    path("polls/", include("polls.urls")),
    # Contatos
    path("contacts/", include("contacts.urls")),
    # Autenticação (login/logout custom)
    path("accounts/", include("accounts.urls")),
]
