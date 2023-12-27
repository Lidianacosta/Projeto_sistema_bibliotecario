from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome_completo = models.CharField(max_length=50, default='')
    telefone = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=250, default='')
    senha = models.CharField(max_length=50, default='')
    nascimento = models.DateField(default=None, null=True,)
    cpf = models.CharField(max_length=14, default='', unique=True)

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
    idade = models.IntegerField()
    estado = models.CharField(max_length=2, default='')
    cidade = models.CharField(max_length=50, default='')
    rua = models.CharField(max_length=50, default='')
    numero = models.IntegerField(default=0)


class Gerente(models.Model):
    class Meta:
        permissions = [
            ('excluir_funcionario', 'pode excluir funcionario'),
            ('aprovar_funcionario', 'pode aprovar funcionario'),
        ]

    senha = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, default='', unique=True)


class Livro(models.Model):
    livro_id = models.IntegerField(default=None, unique=True)
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    ano = models.IntegerField(default=None)
    emprestado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.nome}'


class Emprestimo(models.Model):
    user_name = models.CharField(max_length=50)
    user_cpf = models.CharField(max_length=14, default='')
    livro_info = models.ForeignKey(Livro, on_delete=models.CASCADE)
    emprestimo_data = models.DateField(default=None, null=True)
    devolucao_data = models.DateField(default=None, null=True, blank=True)
