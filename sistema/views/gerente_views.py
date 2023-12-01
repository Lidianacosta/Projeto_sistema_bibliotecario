from django.shortcuts import get_object_or_404, redirect, render
from sistema.models import Funcionario
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


# @permission_required('pode aprovar funcionario', login_url='sistema:login')
def solicitacoes(request, pagina=1):
    solicitacoes = Funcionario.objects.filter(habilitado=False)

    paginator = Paginator(solicitacoes, per_page=5)

    objetos_pagina = paginator.get_page(pagina)

    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_aprovar',
        'link_views_origem': 'sistema:solicitacoes',
        'link_base_html': "global/base_gerente.html",
        'tabela_titulo': 'Funcionários'
    }

    return render(
        request, "sistema/gerente/funcionarios.html",
        context=context
    )


# @permission_required('pode aprovar funcionario', login_url='sistema:login')
def ver_funcionario_aprovar(request, funcionario_id):
    funcionario = get_object_or_404(
        Funcionario, pk=funcionario_id)

    context = {
        'funcionario': funcionario,
        'link_template_voltar': "sistema:solicitacoes",
        'acao_label': "Aprovar",
        'acao_link': "sistema:aprovar",
    }

    return render(
        request,
        'sistema/gerente/aprovar_excluir.html',
        context=context
    )


# @permission_required('pode aprovar funcionario', login_url='sistema:login')
def aprovar(request, funcionario_id):
    if request.method == 'POST':
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        content_type = ContentType.objects.get_for_model(Funcionario)
        permission = Permission.objects.filter(content_type=content_type)

        funcionario.user.user_permissions.set(list(permission))
        funcionario.user.save()
        funcionario.habilitado = True
        funcionario.save()

    return redirect('sistema:solicitacoes')


# @permission_required('pode excluir funcionario', login_url='sistema:login')
def ver_funcionarios(request, pagina=1):
    funcionarios = Funcionario.objects.filter(habilitado=True)

    paginator = Paginator(funcionarios, per_page=5)

    objetos_pagina = paginator.get_page(pagina)

    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_excluir',
        'link_views_origem': 'sistema:funcionarios',
        'link_base_html': "global/base_gerente.html",
        'tabela_titulo': 'Funcionários'
    }

    return render(
        request, "sistema/gerente/funcionarios.html",
        context=context
    )


# @permission_required('pode excluir funcionario', login_url='sistema:login')
def funcionario_excluir(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)

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


# @permission_required('pode excluir funcionario', login_url='sistema:login')
def excluir(request, funcionario_id):
    if request.method == 'POST':
        funcionaro = get_object_or_404(Funcionario, pk=funcionario_id)
        funcionaro.delete()

    return redirect('sistema:funcionarios')
