from django.shortcuts import render
from.form import ContatoForm
from.models import Contato

# Create your views here.
def home(request):
    context = {'mensagem': 'olá mundo'}
    return render(request, 'website/index.html', context)

def homeSite(request):
    context = {'mensagem': 'olá mundo'}
    return render(request, 'website/homeSite.html', context)

def contatos(request):
    mensagem = ''
    if request.method == 'POST':
        try:
            contato = {}
            contato['email'] = request.POST.get('email')
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['titulo'] = request.POST.get('titulo')
            contato['mensagen'] = request.POST.get('mensagen')
            contato['receber'] = True if request.POST('receber') == 'on' else False
            Contato.objects.create(**contato)
        except Exception as e:
              mensagem = str(e)
        else:
              mensagem = 'Contato registrodo com sucesso'

    return render(request, 'website/contato.html', {'mensagem': mensagem})

def envio(request):
    form = ContatoForm()
    contato = Contato.objects.all()
    mensagem = ''
    data = {'mensagem': mensagem, 'form': form, 'contato': contato}
    if request.method == 'POST':
           try:
               form = ContatoForm(request.POST or None)
               if form.is_valid():
                    form.save()
           except Exception as e:
                    mensagem = str(e)
           else:
                    mensagem = 'Contato realizado com sucesso'

    return render(request, 'website/envioContato.html', data)

