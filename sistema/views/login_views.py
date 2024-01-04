from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from rolepermissions.checkers import has_role
from users.roles import Funcionario, Gerente
# Create your views here.


def login(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if has_role(user, Funcionario):
                auth.login(request, user=user)
                return redirect('sistema:cadastrar_usuario')
            if has_role(user, Gerente):
                auth.login(request, user=user)
                return redirect('sistema:solicitacoes')
            messages.warning(request, 'Usuario não autorizado')

    context = {
        'form': form,
        'action_form': 'sistema:login',
        'criar_funcionario': 'sistema:cadastrar_funcionario',
        'criar_gerente': 'sistema:cadastrar_gerente',
        'memu_link_str': 'memu_home',
    }

    return render(
        request,
        "sistema/login.html",
        context=context
    )


def logout(request):
    auth.logout(request)
    return redirect('sistema:login')
