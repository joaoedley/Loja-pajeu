from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nome', 'email', 'nota', 'comentario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'nota': forms.Select(attrs={'class': 'form-select'}, choices=[(i, i) for i in range(1, 6)]),
        }
        labels = {
            'nota': 'Nota (1-5)',
            'comentario': 'Comentário',
        }

class BuscaForm(forms.Form):
    q = forms.CharField(
        label='Buscar produtos',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar...'})
    )