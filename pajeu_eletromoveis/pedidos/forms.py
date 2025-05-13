from django import forms
from django.core.validators import RegexValidator
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['primeiro_nome', 'sobrenome', 'email', 'telefone', 'endereco', 'complemento', 'cep', 'cidade', 'estado', 'tipo_entrega']
        widgets = {
            'tipo_entrega': forms.RadioSelect(),
        }

    def clean(self):
        cleaned_data = super().clean()
        tipo_entrega = cleaned_data.get('tipo_entrega')
        
        # Se for retirada na loja, não precisa validar os campos de endereço
        if tipo_entrega == 'retirada':
            return cleaned_data
            
        # Validação para envio para endereço
        endereco = cleaned_data.get('endereco')
        cep = cleaned_data.get('cep')
        cidade = cleaned_data.get('cidade')
        estado = cleaned_data.get('estado')
        
        if not endereco:
            self.add_error('endereco', 'Este campo é obrigatório.')
        if not cep:
            self.add_error('cep', 'Este campo é obrigatório.')
        if not cidade:
            self.add_error('cidade', 'Este campo é obrigatório.')
        if not estado:
            self.add_error('estado', 'Este campo é obrigatório.')
            
        return cleaned_data

    cep = forms.CharField(
        validators=[RegexValidator(r'^\d{5}-?\d{3}$', 'CEP inválido')],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )