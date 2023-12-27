from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


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
        'action_form': 'sistema:login_funcionario',
        'criar_gerente': 'sistema:cadastrar_funcionario',
        'memu_link_str': 'memu_home',
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
        'action_form': 'sistema:login_gerente',
        'criar_gerente': 'sistema:cadastrar_gerente',
        'memu_link_str': 'memu_home',
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
