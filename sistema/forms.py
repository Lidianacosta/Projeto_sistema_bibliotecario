from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from sistema.models import Funcionario, Livro, Usuario


class GerenteForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('cpf',)
        permissions = [
            'pode aprovar funcionario',
            'pode excluir funcionario',
        ]


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'nome_completo', 'cpf',  'telefone', 'email', 'nascimento',
            'cidade', 'estado', 'instituicao', 'estado', 'cidade', 'rua',
            'numero', 'senha'
        )

        widgets = {
            'senha': forms.PasswordInput(
                attrs={
                    'placeholder': 'infrome sua senha'
                },
            ),
        }

    def save(self, commit: bool = ...):  # type: ignore
        usuario = self.save(commit=False)
        usuario.idade = (date.today() - usuario.nascimento).days // 365
        usuario.save()
        return super().save(commit=True)


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        exclude = ("emprestado",)


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = (
            'nome_completo', 'telefone', 'email', 'nascimento',
            'cpf', 'cidade', 'estado', 'senha'
        )

        widgets = {
            'senha': forms.PasswordInput(
                attrs={
                    'placeholder': 'infrome sua senha',
                },
            ),
            'nascimento': forms.DateInput(),
        }

    def save(self, commit: bool = ...):  # type: ignore
        funcionario = self.save(commit=False)
        funcionario.user = User.objects.create_user(
            cpf=funcionario.cpf,
            password=funcionario.senha
        )
        funcionario.user.user_permissions.clear()
        return super().save(commit=True)
