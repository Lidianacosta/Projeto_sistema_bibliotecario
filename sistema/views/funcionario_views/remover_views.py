from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from sistema.models import Livro, Usuario


def livros_para_excluir(request, pagina=1):
    livros = Livro.objects\
        .filter(emprestado=False).order_by('nome')

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
        ).order_by("nome")

    paginator = Paginator(livros, per_page=5)
    objetos_pagina = paginator.get_page(pagina)
    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_livro_excluir',
        'link_views_origem': "sistema:buscar_livros_excluir",
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
    return redirect('sistema:livros_excluir')


def ver_usuarios(request, pagina=1):
    usuarios = Usuario.objects.all().order_by('nome_completo')

    paginator = Paginator(usuarios, per_page=5)

    objetos_pagina = paginator.get_page(pagina)

    context = {
        'objetos_pagina': objetos_pagina,
        'link_views_acao': 'sistema:ver_usuario',
        'link_views_origem': 'sistema:ver_usuarios',
        'link_base_html': "global/base_funcionario.html",
        'tabela_titulo': 'Usuários',
        'busca_action': 'sistema:busca_usuario'
    }

    return render(
        request,
        'sistema/gerente/funcionarios.html',
        context=context
    )


# @permission_required('pode aprovar funcionario', login_url='sistema:login')
def ver_usuario(request, usuario_id):
    usuario = get_object_or_404(
        Usuario, pk=usuario_id)

    context = {
        'usuario': usuario,
        'link_template_voltar': "sistema:ver_usuarios",
        'acao_label': "Excluir",
        'acao_link': "sistema:deletar_usuario",
    }

    return render(
        request,
        'sistema/funcionario/usuario.html',
        context=context
    )


# @permission_required()
def deletar_usuario(request, usuario_id):

    if request.method == 'POST':
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        usuario.delete()

    return redirect('sistema:ver_usuarios')
