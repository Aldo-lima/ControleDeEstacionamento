from django.urls import path, include
from .views import (home, lista_pessoas, lista_veiculos, lista_movMensalista,
                    lista_movRotativo, lista_mensalista, pessoa_nova, veiculo_novo,
                    mensalista_novo, movMensalista_novo, movRotativo_novo, pessoa_update,
                    veiculo_update, mensalista_update, movMensalista_update, movRotativo_update)

urlpatterns = [

    path('', home, name='core_home'),
    #===========================Pessoas======================================
    path('pessoa', lista_pessoas, name='core_lista_pessoa'),
    path('update_pessoa/<id>', pessoa_update, name='pessoa_update'),
    path('pessoa-nova', pessoa_nova, name='core_pesoa_nova'),
    #==========================Veiculo=======================================
    path('veiculo', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo', veiculo_novo, name='core_veiculo_novo'),
    path('update_veiculo/<id>', veiculo_update, name='core_veiculo_update'),
    #==========================Movimento Mensalista==========================
    path('movMensalista', lista_movMensalista, name='lista_movMensalista'),
    path('movMensalista-novo', movMensalista_novo, name='core_movMensalista_novo'),
    path('update_movMensalista/<id>', movMensalista_update, name='core_movMensalista_update'),
    #==========================Movimento Rotativo============================
    path('movRotativo', lista_movRotativo, name='core_lista_movRotativo'),
    path('movRotativo-novo', movRotativo_novo, name='core_movRotativo_novo'),
    path('update_movRotativo/<id>', movRotativo_update, name='core_movRotativo_update'),
    #==========================Mensalista====================================
    path('mensalista', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista-novo', mensalista_novo, name='core_mensalista_novo'),
    path('update_mensalista/<id>', mensalista_update, name='core_mensalista_update'),
]