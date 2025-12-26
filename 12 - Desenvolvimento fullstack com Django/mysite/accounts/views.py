from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# View de login: autentica usuário via POST e redireciona.
def authenticate_user(request):
    context = {}

    if request.method == "POST":
        # Captura credenciais do formulário
        username = request.POST["username"]
        password = request.POST["password"]
        # Autentica com backend padrão do Django
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Efetua login e redireciona para criação de contato
            login(request, user)
            return HttpResponseRedirect(reverse("contacts:create"))
        else:
            # Erro de autenticação: informa mensagem e re-renderiza template
            context["message"] = "Usuário ou senha inválidos!"
            return render(request, "accounts/login.html", context)

    # GET: exibe o template de login
    return render(request, "accounts/login.html", context)


# View de logout: encerra sessão e volta ao login.
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))
