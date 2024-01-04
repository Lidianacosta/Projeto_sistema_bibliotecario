from django.db import models
from users.models import CustomUser
# Create your models here.


class Funcionario(models.Model):
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    habilitado = models.BooleanField(default=False)


class Usuario(models.Model):
    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    instituicao = models.CharField(max_length=50)


class Livro(models.Model):
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    livro_id = models.PositiveIntegerField(default=None, unique=True)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    ano = models.PositiveIntegerField(default=None)
    emprestado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.nome}'


class Emprestimo(models.Model):
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    user_name = models.CharField(max_length=50)
    user_cpf = models.CharField(max_length=14, default='')
    livro_info = models.ForeignKey(Livro, on_delete=models.CASCADE)
    emprestimo_data = models.DateField(default=None, null=True)
    devolucao_data = models.DateField(default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f'Empréstimo do livro {self.livro_info}'
