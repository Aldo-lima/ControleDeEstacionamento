from django.urls import path, include
from .views import (home, lista_pessoas, lista_veiculos, lista_movMensalista,
                    lista_movRotativo, lista_mensalista, pessoa_nova, veiculo_novo,
                    mensalista_novo, movMensalista_novo, movRotativo_novo, pessoa_update)

urlpatterns = [

    path('', home, name='core_home'),
    path('pessoa', lista_pessoas, name='core_lista_pessoa'),
    path('update_pessoa/<id>', pessoa_update, name='pessoa_update'),
    path('pessoa-nova', pessoa_nova, name='core_pesoa_nova'),
    path('veiculo', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo', veiculo_novo, name='core_veiculo_novo'),
    path('movMensalista', lista_movMensalista, name='lista_movMensalista'),
    path('movMensalista-novo', movMensalista_novo, name='core_movMensalista_novo'),
    path('movRotativo', lista_movRotativo, name='core_lista_movRotativo'),
    path('movRotativo-novo', movRotativo_novo, name='core_movRotativo_novo'),
    path('mensalista', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista-novo', mensalista_novo, name='core_mensalista_novo'),
]