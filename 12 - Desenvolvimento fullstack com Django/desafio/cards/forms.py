from django import forms

from .models import Card


# Formulário baseado no modelo `Card` para capturar dados do titular.
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        # Apenas o `holder_name` é preenchido pelo usuário; demais são gerados.
        fields = ["holder_name"]
