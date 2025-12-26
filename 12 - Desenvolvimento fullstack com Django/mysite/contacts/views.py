from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm, NameForm


# Exige permissão `contacts.add_contact` para criar registros.
@permission_required("contacts.add_contact")
def create(request):
    if request.method == "POST":
        # Formulário baseado em modelo com dados do POST
        form = ContactForm(request.POST)
        if form.is_valid():
            # Acessa dados limpos e salva o modelo
            name = form.cleaned_data["subject"]
            form.save()
            # Redireciona para página de agradecimento com o nome (assunto)
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        # GET: exibe formulário vazio
        form = ContactForm()
    return render(request, "contacts/create.html", {"form": form})


def get_name(request):
    if request.method == "POST":
        # Formulário simples para capturar nome
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["your_name"]
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        # GET: exibe formulário vazio
        form = NameForm()
    return render(request, "contacts/name.html", {"form": form})


def thanks(request, name):
    # Resposta simples com saudação
    return HttpResponse(f"Obrigado {name}!")
