from django.shortcuts import render
from .models import Produto
# Create your views here.

def index2(request):
    produto1 = Produto.objects.filter(nome="Maçã")
    produto2 = Produto.objects.filter(nome="Laranja")
    produto3 = Produto.objects.filter(nome="Morango")
    produto4 = Produto.objects.filter(nome="Banana")
    produto5 = Produto.objects.filter(nome="Alface")
    produto6 = Produto.objects.filter(nome="Couve-flor")
    produto7 = Produto.objects.filter(nome="Brócolis")
    produto8 = Produto.objects.filter(nome="Espinafre")
    produto9 = Produto.objects.filter(nome="Arroz")
    produto10 = Produto.objects.filter(nome="Feijão")
    produto11 = Produto.objects.filter(nome="Grão de Bico")
    produto12 = Produto.objects.filter(nome="Café")
    produto13 = Produto.objects.filter(nome="Leite")
    produto14 = Produto.objects.filter(nome="Vinho")
    produto15 = Produto.objects.filter(nome="Suco")
    produto16 = Produto.objects.filter(nome="Água de coco")
    
    context ={
        'produto1': produto1,
        'produto2': produto2,
        'produto3': produto3,
        'produto4': produto4,
        'produto5': produto5,
        'produto6': produto6,
        'produto7': produto7,
        'produto8': produto8,
        'produto9': produto9,
        'produto10': produto10,
        'produto11': produto11,
        'produto12': produto12,
        'produto13': produto13,
        'produto14': produto14,
        'produto15': produto15,
        'produto16': produto16,
    }
    return render(request,'index2.html', context)

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def produtos(request):
    return render(request,'index2.html')

def produto(request, id):
    prod = Produto.objects.get(id=id)
    context = {
        'produto' : prod
    }
    return render(request,'produto.html',context)
    
def error404(request, exception):
    return render(request,'404.html')

def error500(request):
    return render(request, '500.html')

def carrinho(request):
    return render(request,'carrinho.html')