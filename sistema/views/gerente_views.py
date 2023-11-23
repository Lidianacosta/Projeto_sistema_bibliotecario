from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from sistema.models import Funcionario
from django.core.paginator import Paginator


def solicitacoes(request, pagina=1):
    solicitacoes = Funcionario.objects.filter(habilitado=False)

    paginator = Paginator(solicitacoes, per_page=5)

    objetos_pagina = paginator.get_page(pagina)

    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_aprovar',
        'link_views_origem': 'sistema:solicitacoes'
    }

    return render(
        request, "sistema/gerente/funcionarios.html",
        context=context
    )


def ver_funcionario_aprovar(request, funcionario_id):
    funcionario = get_object_or_404(
        Funcionario, pk=funcionario_id)

    context = {
        'funcionario': funcionario,
        'link_template_voltar': "sistema:solicitacoes",
        'acao_label': "Aprovar",
        'acao_link': "sistema:aprovar"
    }

    return render(
        request,
        'sistema/gerente/aprovar_excluir.html',
        context=context
    )


def aprovar(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, funcionario_id)

    if request.method == 'POST':
        funcionario.habilitado = True
        funcionario.save()

    return redirect('sistema:solicitacoes')


def ver_funcionarios(request, pagina=1):
    funcionarios = Funcionario.objects.filter(habilitado=True)

    paginator = Paginator(funcionarios, per_page=5)

    objetos_pagina = paginator.get_page(pagina)

    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_ecluir',
        'link_views_origem': 'funcionarios'
    }

    return render(
        request, "sistema/gerente/funcionarios.html",
        context=context
    )


def funcionario_excluir(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, funcionario_id)

    context = {
        'funcionario': funcionario,
        'link_template_voltar': "sistema:funcionarios",
        'acao_label': "Excluir",
        'acao_link': "sistema:excluir"
    }

    return render(
        request,
        'sistema/gerente/aprovar_excluir.html',
        context=context
    )


def excluir(request, funcionario_id):
    funcionaro = get_object_or_404(Funcionario, funcionario_id)

    if request.method == 'POST':
        funcionaro.delete()

    return redirect('sistema:funcionarios')
