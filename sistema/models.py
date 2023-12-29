from django.db import models
from users.models import User
from .validator import (validate_cpf, validate_email, validate_name,
                        validate_telefone, validate_nascimento)
# Create your models here.


class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome_completo = models.CharField(
        max_length=50, default='',
        validators=[validate_name]
    )
    telefone = models.CharField(
        max_length=50, default='',
        validators=[validate_telefone]
    )
    email = models.EmailField(
        max_length=250, default='',
        validators=[validate_email]
    )
    nascimento = models.DateField(
        default=None, null=True,
        validators=[validate_nascimento]
    )
    cpf = models.CharField(
        max_length=14, default='', unique=True,
        validators=[validate_cpf]
    )
    senha = models.CharField(max_length=50, default='')

    def __str__(self) -> str:
        return f'{self.nome_completo}'


class Funcionario(Pessoa, models.Model):
    class Meta:
        permissions = [
            ('emprestar', 'pode fazer emprestimo'),
            ('cadastrar_livro', 'pode cadastrar livro'),
            ('excluir_livro', 'pode excluir livro'),
            ('criar_usuario', 'pode criar usuario'),
            ('excluir_usuario', 'pode excluir usuario'),
        ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=False)
    estado = models.CharField(max_length=50)


class Usuario(Pessoa, models.Model):
    instituicao = models.CharField(max_length=50)
    idade = models.PositiveIntegerField(default=None)
    estado = models.CharField(max_length=2, default='')
    cidade = models.CharField(max_length=50, default='')
    rua = models.CharField(max_length=50, default='')
    numero = models.PositiveIntegerField(default=None)


class Livro(models.Model):
    livro_id = models.PositiveIntegerField(default=None, unique=True)
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    ano = models.PositiveIntegerField(default=None)
    emprestado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.nome}'


class Emprestimo(models.Model):
    user_name = models.CharField(max_length=50)
    user_cpf = models.CharField(max_length=14, default='')
    livro_info = models.ForeignKey(Livro, on_delete=models.CASCADE)
    emprestimo_data = models.DateField(default=None, null=True)
    devolucao_data = models.DateField(default=None, null=True, blank=True)
