from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from sistema.models import Funcionario


def solicitacoes(request):
    solicitacoes = Funcionario.objects.filter(habilitado=False)

    context = {
        'funcionarios': solicitacoes,
        'link_template': 'sistema:aprovar'
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
        'acao': "Aprovar"
    }

    return render(
        request,
        'sistema/gerente/aprovar_excluir.html',
        context=context
    )


def aprovar(request, funcionario_id):
    funcionario = Funcionario.objects.get(pk=funcionario_id)

    funcionario.habilitado = True
    funcionario.save()

    return


def ver_funcionarios(request):
    funcionarios = Funcionario.objects.filter(habilitado=True)

    context = {
        'funcionarios': solicitacoes,
        'link_template': 'sistema:excluir'
    }

    return render(
        request, "sistema/gerente/funcionarios.html",
        context=context
    )


def funcionarios_excluir(request, funcionario_id):
    funcionario = Funcionario.objects.get(funcionario_id)

    context = {
        'funcionario': funcionario,
        'link_template_voltar': "sistema:funcionarios",
        'acao': "Excluir"
    }

    return render(
        request,
        'sistema/gerente/aprovar_excluir.html',
        context=context
    )


def excluir(request, funcionario_id):
    funcionaro = get_object_or_404(Funcionario, funcionario_id)

    funcionaro.delete()

    # return redirect(reverse())
