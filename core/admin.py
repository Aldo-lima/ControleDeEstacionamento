from django.contrib import admin
from.models import (Marca, \
    Veiculo,\
    Pessoa, \
    Parametros, \
    ModelRotativo,\
    Mensalista, \
    MovMensalista)

class MovRotativoAdimin(admin.ModelAdmin):
    list_display = (
         'veiculo', 'checkin', 'checkout', 'valor_hora', 'hora_total', 'total', 'pago')
    def veiculo(self, obj):
        return obj.veiculo

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'data_pagamento', 'total')


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(ModelRotativo, MovRotativoAdimin)
