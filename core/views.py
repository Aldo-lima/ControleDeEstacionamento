from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovMensalista, ModelRotativo, Mensalista
from .form import (PessoaForm, VeiculoForm, MensalistaForm,
                   MovRotativoForm,  MovMensalistaForm)
# Create your views here.

def home(request):
    context = {'mensagem': 'olá mundo'}
    return render(request, 'core/index.html', context)

#========================Pessoas==========================

def lista_pessoas(request):
    form = PessoaForm()
    pessoas = Pessoa.objects.all()
    data = {'pessoas': pessoas, 'form':form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_nova(request, id):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoa')


def pessoa_update(request, id):
        data = {}
        pessoa = Pessoa.objects.get(id=id)
        form = PessoaForm(request.POST or None, instance=pessoa)
        data['pessoa'] = pessoa
        data['form'] = form

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('core_lista_pessoa')
        else:
            return render(request, 'core/up_date_pessoa.html', data)

#====================================Veiculo=======================

def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos':veiculos, 'form': form}
    return render(request, 'core/lista_veiculo.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


#==================================Movimento Mensalista


def lista_movMensalista(request):
    form = MovMensalistaForm()
    movMensalistas = MovMensalista.objects.all()
    data = {'movMensalistas': movMensalistas, 'form': form}
    return render(request, 'core/lista_MovMensalistas.html', data)

def movMensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movMensalista')

def lista_movRotativo(request):
    form =MovRotativoForm()
    movRotativos = ModelRotativo.objects.all()
    data = {'movRotativos':movRotativos, 'form': form}
    return render(request, 'core/lista_MovRotativo.html', data)

def movRotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movRotativo')

def lista_mensalista(request):
     form = MensalistaForm()
     mensalistas = Mensalista.objects.all()
     data = {'mensalistas': mensalistas, 'form': form}
     return render(request, 'core/lista_mensalista.html', data)

def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')