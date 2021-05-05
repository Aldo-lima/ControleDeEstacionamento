from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovMensalista, ModelRotativo, Mensalista
# Create your views here.

def home(request):
    context = {'mensagem': 'olá mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas':pessoas})

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculo.html', {'veiculos':veiculos})

def lista_movMensalista(request):
    movMensalistas = MovMensalista.objects.all()
    return render(request, 'core/lista_MovMensalistas.html', {'movMensalistas':movMensalistas})

def lista_movRotativo(request):
    movRotativos = ModelRotativo.objects.all()
    return render(request, 'core/lista_MovRotativo.html', {'movRotativos':movRotativos})

def lista_movRotativo(request):
    movRotativos = ModelRotativo.objects.all()
    return render(request, 'core/lista_MovRotativo.html', {'movRotativos':movRotativos})

def lista_mensalista(request):
     mensalistas = Mensalista.objects.all()
     return render(request, 'core/lista_mensalista.html', {'mensalistas':mensalistas})