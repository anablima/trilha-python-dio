from django import forms

from .models import Contact


# Formulários: um simples (`NameForm`) e um baseado em modelo (`ContactForm`).
class NameForm(forms.Form):
    # Campo de texto com rótulo e limite de caracteres.
    your_name = forms.CharField(label="Seu nome", max_length=100)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # Inclui todos os campos do modelo `Contact` no formulário.
        fields = "__all__"
