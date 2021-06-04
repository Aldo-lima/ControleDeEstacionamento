from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pessoa, Veiculo, MovMensalista, ModelRotativo, Mensalista
from .form import (PessoaForm, VeiculoForm, MensalistaForm,
                   MovRotativoForm,  MovMensalistaForm)
# Create your views here.

def home(request):
    context = {'mensagem': 'olá mundo'}
    return render(request, 'core/index.html', context)

#========================Pessoas==========================
@login_required()
def lista_pessoas(request):
    form = PessoaForm()
    pessoas = Pessoa.objects.all()
    data = {'pessoas': pessoas, 'form':form}
    return render(request, 'core/lista_pessoas.html', data)

@login_required()
def pessoa_nova(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoa')

@login_required()
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
@login_required()
def pessoa_delete(request, id ):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == "POST":
        pessoa.delete()
        return redirect('core_lista_pessoa')
    else:
        return render(request, 'core/delete_confirme.html', {'obj': pessoa})

#====================================Veiculo=======================
@login_required()
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculo.html', data)
@login_required()
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')
@login_required()
def veiculo_update(request, id):
        data = {}
        veiculo = Veiculo.objects.get(id=id)
        form = VeiculoForm(request.POST or None, instance=veiculo)
        data['veiculo'] = veiculo
        data['form'] = form

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('core_lista_veiculos')
        else:
            return render(request, 'core/update_veiculo.html', data)
@login_required()
def veiculo_delete(request, id ):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == "POST":
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirme.html', {'obj': veiculo})
#==================================Movimento Mensalista===================

@login_required
def lista_movMensalista(request):
    form = MovMensalistaForm()
    movMensalistas = MovMensalista.objects.all()
    data = {'movMensalistas': movMensalistas, 'form': form}
    return render(request, 'core/lista_MovMensalistas.html', data)
@login_required
def movMensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movMensalista')

@login_required
def movMensalista_update(request, id):
        data = {}
        movMensalista = MovMensalista.objects.get(id=id)
        form = MovMensalistaForm(request.POST or None, instance=movMensalista)
        data['movMensalista'] = movMensalista
        data['form'] = form

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('lista_movMensalista')
        else:
            return render(request, 'core/update_movMensalista.html', data)

@login_required
def movMensalista_delete(request, id ):
    movMensalista = MovMensalista.objects.get(id=id)
    if request.method == "POST":
        movMensalista.delete('lista_movMensalista')
        return redirect()
    else:
        return render(request, 'core/delete_confirme.html', {'obj': movMensalista})

#============================Movimento Rotativo=========================
@login_required()
def lista_movRotativo(request):
    form =MovRotativoForm()
    movRotativos = ModelRotativo.objects.all()
    data = {'movRotativos':movRotativos, 'form': form}
    return render(request, 'core/lista_MovRotativo.html', data)
@login_required()
def movRotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movRotativo')
@login_required()
def movRotativo_update(request, id):
        data = {}
        movRotativo = ModelRotativo.objects.get(id=id)
        form = MovRotativoForm(request.POST or None, instance=movRotativo)
        data['movRotativo'] = movRotativo
        data['form'] = form

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('core_lista_movRotativo')
        else:
            return render(request, 'core/update_movRotativo.html', data)

@login_required()
def movRotativo_delete(request, id ):
    movRotativo = ModelRotativo.objects.get(id=id)
    if request.method == "POST":
        movRotativo.delete()
        return redirect('core_lista_movRotativo')
    else:
        return render(request, 'core/delete_confirme.html', {'obj': movRotativo})

#======================================Mensalista===================
@login_required()
def lista_mensalista(request):
     form = MensalistaForm()
     mensalistas = Mensalista.objects.all()
     data = {'mensalistas': mensalistas, 'form': form}
     return render(request, 'core/lista_mensalista.html', data)
@login_required()
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')
@login_required()
def mensalista_update(request, id):
        data = {}
        mensalista = Mensalista.objects.get(id=id)
        form = MensalistaForm(request.POST or None, instance=mensalista)
        data['mensalista'] = mensalista
        data['form'] = form

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('core_lista_mensalista')
        else:
            return render(request, 'core/update_mensalista.html', data)

@login_required()
def mensalista_delete(request, id ):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == "POST":
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirme.html', {'obj': mensalista})