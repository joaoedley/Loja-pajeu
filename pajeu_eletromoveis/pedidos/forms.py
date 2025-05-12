from django import forms
from django.core.validators import RegexValidator
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido  
        fields = ['primeiro_nome', 'sobrenome', 'email', 'endereco', 
                 'complemento', 'cep', 'cidade', 'estado', 'telefone',
                 'tipo_entrega']
        
        ESTADOS_CHOICES = [
            ('', 'Selecione...'),
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        ]
        
        widgets = {
            'primeiro_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}, choices=ESTADOS_CHOICES),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_entrega': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
    
    cep = forms.CharField(
        validators=[RegexValidator(r'^\d{5}-?\d{3}$', 'CEP inválido')],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )