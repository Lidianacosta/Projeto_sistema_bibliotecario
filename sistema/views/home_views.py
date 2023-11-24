
from django.shortcuts import redirect, render
from sistema.forms import FuncionarioForm, GerenteForm, LivroForm, UsuarioForm
from sistema.models import Funcionario, Gerente
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def cadastra_funcionario(request):

    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('sistema:cadastra_funcionario')

    context = {
        'form': form,
        'action_form': 'sistema:cadastra_funcionario',
        'caminho_extender': "global/base.html"
    }

    return render(
        request,
        "sistema/form.html",
        context=context
    )


def login(request):
    form = AuthenticationForm(request)
    context = {
        'form': form,
        'action_form': 'sistema:login',
        'caminho_extender': "global/base.html"
    }

    return render(
        request,
        "sistema/form.html",
        context=context
    )
