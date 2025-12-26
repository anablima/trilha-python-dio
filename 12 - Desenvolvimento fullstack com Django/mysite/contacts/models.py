from django.db import models


# Modelo simples de contato com assunto, mensagem e remetente.
class Contact(models.Model):
    # Assunto do contato
    subject = models.CharField(max_length=100)
    # Corpo da mensagem
    message = models.CharField(max_length=250)
    # Email do remetente
    sender = models.EmailField()
    # Marcar para enviar cópia ao próprio remetente (opcional)
    cc_myself = models.BooleanField(null=True, blank=True)
