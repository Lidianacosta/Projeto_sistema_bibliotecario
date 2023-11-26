from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from sistema.models import Livro, Usuario


def livros_para_excluir(request, pagina=1):
    livros = Livro.objects\
        .filter(emprestado=False)

    paginator = Paginator(livros, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_livro_excluir',
        'link_views_origem': "sistema:livros_excluir",
        'link_busca': 'sistema:buscar_livros_excluir',
        'link_base_html': "global/base_funcionario.html"
    }

    return render(
        request,
        "sistema/funcionario/livros.html",
        context=context
    )


def buscar_livro_para_excluir(request, pagina=1):
    buscado = request.GET.get('q', '').strip()

    if not buscado:
        return redirect('sistema:')

    livros = Livro.objects\
        .filter(emprestado=False)\
        .filter(
            Q(nome__icontains=buscado) |
            Q(livro_id__icontains=buscado) |
            Q(autor__icontains=buscado) |
            Q(editora__icontains=buscado) |
            Q(ano__icontains=buscado)
        )

    paginator = Paginator(livros, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_livro_excluir',
        'link_views_origem': "sistema:livros_excluir",
        'link_busca': 'sistema:buscar_livros_excluir',
        'link_base_html': "global/base_funcionario.html"
    }

    return render(
        request,
        "sistema/funcionario/livros.html",
        context=context
    )


def ver_livro_excluir(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    context = {
        'livro': livro,
        'link_view_voltar': 'sistema:livros_excluir',
        'acao_label': "Excluir Livro",
        'link_acao': 'sistema:excluir',
        'link_base_html': "global/base_funcionario.html"
    }

    return render(
        request,
        "sistema/funcionario/acao_livro.html",
        context=context
    )


def excluir_livro(request, livro_id):
    if request.method == 'POST':
        livro = get_object_or_404(Livro, pk=livro_id)
        livro.delete()


def ver_usuarios(request):
    return render(
        request,
        'sistema/funcionario/usuario.html',
    )


def ver_usuario():
    pass
