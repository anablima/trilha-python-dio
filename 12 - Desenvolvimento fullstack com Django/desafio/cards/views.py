from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CardForm
from .models import Card


# Exige autenticação para solicitar um cartão.
@login_required
def request_card(request):
    # Gera dados fictícios de cartão para demonstrar o fluxo.
    def generate_card_info() -> dict[str, str]:
        import random
        from datetime import UTC, datetime

        cc_month = str(random.randint(1, 12)).zfill(2)
        cc_year = str(datetime.now(UTC).year + 10)[2:]
        return {
            "name": "DIO Bank Platinum",
            "number": "".join([str(random.randint(0, 9)) for _ in range(16)]),
            "network": random.choice(["V", "M"]),
            "expiration_date": f"{cc_month}/{cc_year}",
            "cvv": "".join([str(random.randint(0, 9)) for _ in range(3)]),
        }

    if request.method == "POST":
        # Bind dos dados enviados ao formulário
        form = CardForm(request.POST)
        if form.is_valid():
            # Preenche os campos gerados automaticamente (nome, número, etc.)
            card_info = generate_card_info()

            # `commit=False` para completar campos antes de salvar
            card_request = form.save(commit=False)
            card_request.user = request.user
            card_request.name = card_info["name"]
            card_request.number = card_info["number"]
            card_request.network = card_info["network"]
            card_request.expiration_date = card_info["expiration_date"]
            card_request.cvv = card_info["cvv"]
            card_request.save()

            # Redireciona para a lista de requisições do usuário
            return redirect(reverse("cards:view_requests"))
    else:
        # Requisição GET: inicializa formulário vazio
        form = CardForm()
    return render(request, "cards/request_card.html", {"form": form})


# Lista solicitações do usuário autenticado, mais recentes primeiro.
@login_required
def view_requests(request):
    user_requests = Card.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "cards/view_requests.html", {"user_requests": user_requests})


# Detalhes de uma solicitação específica do usuário.
@login_required
def card_details(request, card_id):
    card = get_object_or_404(Card, id=card_id, user=request.user)
    return render(request, "cards/card_details.html", {"card": card})
