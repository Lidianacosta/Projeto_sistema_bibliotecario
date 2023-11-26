from django.shortcuts import render, redirect
from sistema.forms import LivroForm, UsuarioForm


def cadastrar_usuario(request):

    form = UsuarioForm()

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('sistema:cadastra_usuario')

    context = {
        'form': form,
        'action_form': 'sistema:cadastra_usuario',
        'caminho_extender': "global/base_funcionario.html"
    }

    return render(
        request,
        "sistema/form.html",
        context=context
    )


def cadastrar_livro(request):
    form = LivroForm()

    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('sistema:cadastra_livro')

    context = {
        'form': form,
        'action_form': 'sistema:cadastra_livro',
        'caminho_extender': "global/base_funcionario.html"
    }

    return render(
        request,
        "sistema/form.html",
        context=context
    )
