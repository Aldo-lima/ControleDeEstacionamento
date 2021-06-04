from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'mensagem': 'olá mundo'}
    return render(request, 'website/index.html', context)