from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistema.models import Funcionario, Livro, Usuario
import re


class GerenteForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        permissions = [
            'pode aprovar funcionario',
            'pode excluir funcionario',
        ]


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

        widgets = {
            'senha': forms.PasswordInput(
                attrs={
                    'placeholder': 'infrome sua senha'
                },
            ),
        }


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        # fields = ("",)
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
                    'placeholder': 'infrome sua senha'
                },
            ),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        # self.add_error(
        #     'nome_completo',
        #     ValidationError(
        #         'mesagem de error 2',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'nome_completo',
        #     ValidationError(
        #         message='mesagem de error',
        #     )
        # )

        return super().clean()

    def clean_nome_completo(self):
        nome_completo = self.cleaned_data.get('nome_completo')

        # validacao

        return nome_completo

    def save(self, commit: bool = ...):
        funcionario = self.save(commit=False)
        funcionario.user = User.objects.create_user(
            username=funcionario.cpf,
            password=funcionario.senha
        )
        funcionario.user.user_permissions.clear()
        return super().save(commit=True)
