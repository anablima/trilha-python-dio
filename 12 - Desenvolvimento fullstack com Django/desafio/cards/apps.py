from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cards"
    # Nome amigável do app exibido no admin
    verbose_name = "Cartão"
