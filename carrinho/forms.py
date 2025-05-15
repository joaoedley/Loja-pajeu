from django import forms

class AdicionarProdutoCarrinhoForm(forms.Form):
    quantidade = forms.IntegerField(
        min_value=1,
        max_value=99,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 60px'})
    )
    sobrepor = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )