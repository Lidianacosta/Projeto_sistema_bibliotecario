from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.db.models import Q

from .funcionario_views.emprestimo_views import EmprestimoListView, \
    LivroListView, StatusEmprestimoListView, PER_PAGE
from .gerente_views import FuncionarioListView
from .funcionario_views.remover_views import UsuarioListView


class SearchLivroEmprestarListView(LivroListView):

    search_value = ''
    redirect_url = 'sistema:livros_emprestar'

    def get(self, request: HttpRequest, *args,
            **kwargs) -> HttpResponse:
        self.search_value = request.GET.get('q', '').strip()
        if not self.search_value:
            return redirect(self.redirect_url)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        search_value = self.search_value

        return super().get_queryset().filter(emprestado=False)\
            .filter(
            Q(nome__icontains=search_value) |
            Q(livro_id__icontains=search_value) |
            Q(autor__icontains=search_value) |
            Q(editora__icontains=search_value) |
            Q(ano__icontains=search_value)
        ).order_by('nome')[:PER_PAGE]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "search_value": self.search_value
        })
        return context


class SearchLivroExcluirListView(SearchLivroEmprestarListView):
    redirect_url = 'sistema:livros_excluir'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_livro_excluir',
            'link_busca': 'sistema:buscar_livros_excluir',
            'link_base_html': "global/base_funcionario.html"
        })
        return context


class SearchEmprestimoListView(EmprestimoListView):
    search_value = ''
    redirect_url = 'sistema:ver_emprestimos'

    def get(self, request: HttpRequest, *args,
            **kwargs) -> HttpResponse:
        self.search_value = request.GET.get('q', '').strip()
        if not self.search_value:
            return redirect(self.redirect_url)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        search_value = self.search_value

        return super().get_queryset().exclude(devolucao_data__isnull=True) \
            .filter(
            Q(user_name__icontains=search_value) |
            Q(user_cpf__icontains=search_value) |
            Q(emprestimo_data__icontains=search_value) |
            Q(livro_info__nome__icontains=search_value)
        )[:PER_PAGE]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "search_value": self.search_value,
        })
        return context


class SearchStatusEmprestimoListView(StatusEmprestimoListView):
    search_value = ''
    redirect_url = 'sistema:status_emprestimo'

    def get(self, request: HttpRequest, *args,
            **kwargs) -> HttpResponse:
        self.search_value = request.GET.get('q', '').strip()
        if not self.search_value:
            return redirect(self.redirect_url)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        search_value = self.search_value

        return super().get_queryset().filter(devolucao_data__isnull=True) \
            .filter(
            Q(user_name__icontains=search_value) |
            Q(user_cpf__icontains=search_value) |
            Q(emprestimo_data__icontains=search_value) |
            Q(livro_info__nome__icontains=search_value)
        )[:PER_PAGE]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "search_value": self.search_value,
            'link_views_acao': 'sistema:ver_status_emprestimo',
            'link_views_origem': 'sistema:buscar_status_emprestimo',
        })
        return context


class SearchRenovarEmprestimoListView(SearchStatusEmprestimoListView):
    redirect_url = "sistema:ver_emprestimo_renovar"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_revovar_emprestimo',
            'link_views_origem': 'sistema:buscar_emprestimo_renovar'
        })
        return context


class SearchUsuarioListView(UsuarioListView):
    search_value = ''
    redirect_url = 'sistema:ver_usuarios'

    def get(self, request: HttpRequest, *args,
            **kwargs) -> HttpResponse:
        self.search_value = request.GET.get('q', '').strip()
        if not self.search_value:
            return redirect(self.redirect_url)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        search_value = self.search_value

        return super().get_queryset()\
            .filter(
            Q(instituicao__icontains=search_value) |
            Q(nome_completo__icontains=search_value) |
            Q(cpf__icontains=search_value) |
            Q(email__icontains=search_value)
        )[:PER_PAGE]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "search_value": self.search_value,
        })
        return context


class SearchFuncionarioListView(FuncionarioListView):
    search_value = ''
    redirect_url = 'sistema:funcionarios'

    def get(self, request: HttpRequest, *args,
            **kwargs) -> HttpResponse:
        self.search_value = request.GET.get('q', '').strip()
        if not self.search_value:
            return redirect(self.redirect_url)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        search_value = self.search_value

        return super().get_queryset()\
            .filter(
            Q(estado__icontains=search_value) |
            Q(nome_completo__icontains=search_value) |
            Q(cpf__icontains=search_value) |
            Q(email__icontains=search_value)
        )[:PER_PAGE]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "search_value": self.search_value,
        })
        return context
