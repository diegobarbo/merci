from django import forms
from .models import Peca, Venda


class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome', 'categoria', 'quantidade']


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['peca', 'venda_quantidade']