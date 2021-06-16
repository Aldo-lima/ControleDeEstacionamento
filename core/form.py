
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import (Pessoa,
                     Veiculo,
                     Mensalista,
                     MovMensalista,
                     ModelRotativo)





class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]



class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields= '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class MovRotativoForm(ModelForm):
    class Meta:
        model = ModelRotativo
        fields = '__all__'

class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'