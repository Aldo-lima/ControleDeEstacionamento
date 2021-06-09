
from django.urls import path, include
from.views import  home, contatos, envio, homeSite
urlpatterns = [
path('', home, name='site_home'),
path('homeSite', homeSite, name='site_homeSite'),
path('contato', contatos, name='website_contato'),
path('envio', envio, name='website_envio'),
]