from django.db import models
from cpf_field.models import CPFField  # https://pypi.org/project/django-cpf/
# Create your models here.


class Pessoa(models.Model):
    class Meta:  # https://code.djangoproject.com/wiki/ComoHerdarClassesDeModelo
        abstract = True

    nome_completo = models.CharField(max_length=50, default='')
    telefone = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=250, default='')
    senha = models.CharField(max_length=50, default='')
    nascimento = models.DateField(default=None)
    cpf = CPFField('cpf', default='')

    def __str__(self) -> str:
        return f'{self.nome_completo}'


class Endereco(models.Model):
    estado = models.CharField(max_length=2, default='')
    cidade = models.CharField(max_length=50, default='')
    rua = models.CharField(max_length=50, default='')
    numero = models.IntegerField(default=0)


class Funcionario(Pessoa, models.Model):
    cidade = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=False)
    estado = models.CharField(max_length=50)


class Usuario(Pessoa, models.Model):
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, default=None)
    instituicao = models.CharField(max_length=50)
    idade = models.IntegerField()


class Gerente(models.Model):
    senha = models.CharField(max_length=50)
    cpf = CPFField('cpf')


class Livro(models.Model):
    livro_id = models.IntegerField(default=0)
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    ano = models.IntegerField(default=0)
    emprestado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.nome}'


class Emprestimo(models.Model):
    user_name = models.CharField(max_length=50)
    user_cpf = CPFField('cpf')
    livro_info = models.CharField(max_length=50, default='')
    emprestimo_data = models.DateTimeField(default=None)
    status = models.CharField(max_length=50, default='')
    devolucao_data = models.DateTimeField(default=None,)
