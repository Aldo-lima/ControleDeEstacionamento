from django.db import models


class Contato(models.Model):
    dataEnvio = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    mensagem = models.TextField()
    receber = models.BooleanField()

    def __stf__(self):
        return self.nome


