from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from sistema.forms import FuncionarioForm, GerenteForm
from sistema.models import Gerente
# Create your views here.


def cadastrar_funcionario(request):

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


def login_funcionario(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user=user)
            redirect('sistema:cadastrar_usuario')

    context = {
        'form': form,
        'action_form': 'sistema:login',
        'caminho_extender': "global/base.html",
        'criar_gerente': 'sistema:cadastrar_funcionario'
    }

    return render(
        request,
        "sistema/login.html",
        context=context
    )


def login_gerente(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user=user)
            redirect('sistema:solicitacoes')

    context = {
        'form': form,
        'action_form': 'sistema:login',
        'caminho_extender': "global/base.html",
        'criar_gerente': 'sistema:cadastrar_gerente'
    }

    return render(
        request,
        "sistema/login.html",
        context=context
    )


def logout_gerente(request):
    auth.logout(request)
    return redirect('sistema:login_gerente')


def logout_funcionario(request):
    auth.logout(request)
    return redirect('sistema:login_funcionario')


def cadastrar_gerente(request):
    form = GerenteForm()

    if request.method == 'POST':
        form = GerenteForm(request.POST)
        gerente = Gerente.objects.all()
        if len(gerente) == 0:
            if form.is_valid():
                user = form.save(commit=False)
                gerente = Gerente(senha=user.password, cpf=user.username)
                form.save(commit=True)

            return redirect('sistema:login_gerente')

    context = {
        'form': form,
        'action_form': 'sistema:login',
        'caminho_extender': "global/base.html",
    }

    return render(
        request,
        "sistema/form.html",
        context=context
    )
