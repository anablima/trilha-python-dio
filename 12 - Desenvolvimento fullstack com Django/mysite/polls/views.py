from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.models import Choice, Question


# Página inicial: lista últimas 5 perguntas por data de publicação.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


# Detalhe de uma pergunta específica.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


# Resultado de votos da pergunta informada.
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


# Processa voto: incrementa opção selecionada e redireciona para resultados.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Busca opção pelo ID enviado via POST
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Se nenhuma opção foi escolhida, reexibe detalhe com erro
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Você não selecionou nenhuma opção.",
            },
        )
    else:
        # Incrementa votos e salva; em seguida, redireciona para resultados
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
