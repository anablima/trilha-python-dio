from django.contrib.auth.models import User
from django.db import models


# Modelo de cartão vinculado a `User` com metadados e status.
class Card(models.Model):
    # Opções de status: armazenamos um código e exibimos um rótulo amigável.
    STATUS_CHOICES = (
        ("P", "Pendente"),
        ("A", "Aprovado"),
        ("E", "Enviado"),
        ("R", "Recebido"),
    )

    # Bandeiras possíveis da rede do cartão (Visa/Mastercard).
    CARD_NETWORK = (
        ("V", "Visa"),
        ("M", "Mastercard"),
    )

    # Relacionamento com usuário; `PROTECT` evita excluir usuário com cartões.
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cards", verbose_name="Usuário")
    # Nome comercial do cartão emitido
    name = models.CharField("Nome", max_length=20)
    # Número do cartão (apenas fins didáticos; em produção, nunca armazenar em texto puro)
    number = models.CharField("Número", max_length=16)
    # Nome do portador impresso no cartão
    holder_name = models.CharField("Titular", max_length=20)
    # Rede/bandeira do cartão (choices)
    network = models.CharField("Rede", max_length=1, choices=CARD_NETWORK)
    # Validade no formato MM/YY
    expiration_date = models.CharField("Data de expiração", max_length=5)
    # Código de segurança (CVV) — não armazenar em produção
    cvv = models.CharField("CVV", max_length=4)
    # Status do pedido com valor padrão "Pendente"
    status = models.CharField("Status", max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    # Carimbos de criação/alteração gerenciados pelo Django
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Alterado em", auto_now=True)

    def __str__(self) -> str:
        # Exibição amigável no admin e listas
        return f"Cartão {self.id} - {self.user.username} - {self.get_status_display()}"

    class Meta:
        # Nome plural amigável e ordenação por mais recente
        verbose_name_plural = "Cartões"
        ordering = ["-created_at"]
