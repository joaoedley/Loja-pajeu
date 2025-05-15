from .models import Categoria

def categorias_disponiveis(request):
    return {
        'categorias_menu': Categoria.objects.all()
    } 