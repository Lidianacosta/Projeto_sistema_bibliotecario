from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import date
from sistema.models import Emprestimo, Livro, Usuario


def livros_para_empretar(request, pagina=1):
    livros = Livro.objects.filter(emprestado=False).order_by('nome')

    paginator = Paginator(livros, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_origem': 'sistema:livros_emprestar',
        'link_views_acao': 'sistema:ver_livro_emprestar',
        'link_busca': 'sistema:buscar_livros_emprestar',
        'link_base_html': "global/base_emprestimo.html"
    }

    return render(request, "sistema/funcionario/livros.html", context=context)


def buscar_livro_para_emprestar(request, pagina=1):
    buscado = request.GET.get('q', '').strip()

    if not buscado:
        return redirect('sistema:livros_emprestar')

    livros = Livro.objects\
        .filter(emprestado=False)\
        .filter(
            Q(nome__icontains=buscado) |
            Q(livro_id__icontains=buscado) |
            Q(autor__icontains=buscado) |
            Q(editora__icontains=buscado) |
            Q(ano__icontains=buscado)
        ).order_by('nome')

    paginator = Paginator(livros, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_origem': 'sistema:buscar_livros_emprestar',
        'link_views_acao': 'sistema:ver_livro_emprestar',
        'link_busca': 'sistema:buscar_livros_emprestar',
        'link_base_html': "global/base_emprestimo.html"
    }

    return render(request, "sistema/funcionario/livros.html", context=context)


def ver_livro_emprestar(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    context = {
        'livro': livro,
        'link_view_voltar': 'sistema:livros_emprestar',
        'acao_label': "Emprestar",
        'link_acao': 'sistema:emprestar',
        'link_base_html': "global/base_emprestimo.html",
        'title': 'Emprestar'
    }

    return render(request,
                  "sistema/funcionario/acao_livro.html",
                  context=context)


def realizar_emprestimo(request, livro_id):

    if request.method == 'POST':
        cpf = request.POST.get('cpf', '')
        senha = request.POST.get('senha', '')
        usuario = Usuario.objects.filter(
            cpf__iexact=cpf, senha__iexact=senha)[0]

        if not usuario:
            return redirect('sistema:ver_livro_emprestar')

        emprestimo = Emprestimo()
        emprestimo.user_cpf = cpf
        emprestimo.user_name = usuario.nome_completo
        emprestimo.emprestimo_data = date.today()
        emprestimo.livro_info = get_object_or_404(Livro, pk=livro_id)
        emprestimo.livro_info.emprestado = True
        emprestimo.livro_info.save()
        emprestimo.save()

    return redirect('sistema:livros_emprestar')


# emprestimo


def emprestimos(request, pagina=1):
    emprestimos_objetos = Emprestimo.objects \
        .exclude(devolucao_data=None)

    paginator = Paginator(emprestimos_objetos, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_emprestimo',
        'link_views_origem': 'sistema:ver_emprestimos',
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimos.html",
                  context=context)


def buscar_emprestimos(request, pagina=1):
    buscado = request.GET.get('q', '').strip()
    emprestimos_objetos = Emprestimo.objects\
        .exclude(devolucao_data=None) \
        .filter(
            Q(user_name__icontains=buscado) |
            Q(user_cpf__icontains=buscado) |
            Q(emprestimo_data__icontains=buscado)
        )

    paginator = Paginator(emprestimos_objetos, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_emprestimo',
        'link_views_origem': 'sistema:busca_emprestimos'
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimos.html",
                  context=context)


def ver_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    context = {
        'emprestimo': emprestimo,
        'link_voltar': 'sistema:ver_emprestimos',
        'title': 'emprestimo'
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimo.html",
                  context=context)


def status_emprestimo(request, pagina=1):
    emprestimos_objetos = Emprestimo.objects\
        .filter(devolucao_data=None)

    paginator = Paginator(emprestimos_objetos, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_status_emprestimo',
        'link_views_origem': 'sistema:status_emprestimo',
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimos.html",
                  context=context)


def buscar_status_emprestimo(request, pagina=1):
    buscado = request.GET.get('q', '').strip()
    emprestimos_objetos = Emprestimo.objects\
        .filter(devolucao_data=None) \
        .filter(
            Q(user_name__icontains=buscado) |
            Q(user_cpf__icontains=buscado) |
            Q(emprestimo_data__icontains=buscado) |
            Q(devolucao_data__icontains=buscado)
        )

    paginator = Paginator(emprestimos_objetos, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_status_emprestimo',
        'link_views_origem': 'sistema:buscar_status_emprestimo'
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimos.html",
                  context=context)


def ver_status_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    context = {
        'emprestimo': emprestimo,
        'link_voltar': 'sistema:status_emprestimo',
        'link_acao': 'sistema:devolver_livro',
        'acao_label': 'Devolver'
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimo.html",
                  context=context)


def devolver_livro(request, emprestimo_id):
    if request.method == 'POST':
        emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

        emprestimo.devolucao_data = date.today()
        emprestimo.livro_info.emprestado = False
        emprestimo.livro_info.save()
        emprestimo.save()

    return redirect('sistema:status_emprestimo')


def ver_emprestimo_renovar(request, pagina=1):
    emprestimos_objetos = Emprestimo.objects \
        .filter(devolucao_data=None)

    paginator = Paginator(emprestimos_objetos, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_revovar_emprestimo',
        'link_views_origem': 'sistema:ver_emprestimo_renovar',
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimos.html",
                  context=context)


def buscar_emprestimo_renovar(request, pagina=1):
    buscado = request.GET.get('q', '').strip()
    emprestimos_objetos = Emprestimo.objects\
        .filter(devolucao_data=None) \
        .filter(
            Q(user_name__icontains=buscado) |
            Q(user_cpf__icontains=buscado) |
            Q(emprestimo_data__icontains=buscado) |
            Q(devolucao_data__icontains=buscado)
        )

    paginator = Paginator(emprestimos_objetos, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_revovar_emprestimo',
        'link_views_origem': 'sistema:buscar_emprestimo_renovar'
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimos.html",
                  context=context)


def ver_revovar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    context = {
        'emprestimo': emprestimo,
        'link_voltar': 'sistema:ver_emprestimo_renovar',
        'link_acao': 'sistema:renovar_emprestimo',
        'acao_label': 'Renovar'
    }

    return render(request,
                  "sistema/funcionario/emprestimo/emprestimo.html",
                  context=context)


def renovar_emprestimo(request, emprestimo_id):
    if request.method == 'POST':
        emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

        emprestimo.devolucao_data = date.today()
        emprestimo.save()
        novo_emprestimo = Emprestimo(
            user_name=emprestimo.user_name,
            user_cpf=emprestimo.user_cpf,
            livro_info=emprestimo.livro_info,
            emprestimo_data=date.today(),
        )
        novo_emprestimo.save()

    return redirect('sistema:ver_emprestimo_renovar')
