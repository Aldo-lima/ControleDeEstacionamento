from django.urls import path, include
from .views import (home, lista_pessoas, lista_veiculos, lista_movMensalista,
                    lista_movRotativo, lista_mensalista)

urlpatterns = [

    path('', home, name='core_home'),
    path('pessoa', lista_pessoas, name='core_lista_pessoa'),
    path('veiculo', lista_veiculos, name='lista_veiculos'),
    path('movMensalista', lista_movMensalista, name='lista_movMensalista'),
    path('movRotativo', lista_movRotativo, name='lista_movRotativo'),
    path('mensalista', lista_mensalista, name='lista_mensalista'),
]