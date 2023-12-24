from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from datetime import date
from django.contrib import messages
from django.views.generic import ListView, DetailView
from sistema.models import Emprestimo, Livro, Usuario

PER_PAGE = 4


class LivroListView(ListView):
    model = Livro
    paginate_by = PER_PAGE
    template_name = "sistema/funcionario/livros.html"

    def get_queryset(self):
        return super().get_queryset().filter(emprestado=False).order_by("nome")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_livro_emprestar',
            'link_busca': 'sistema:buscar_livros_emprestar',
            'link_base_html': "global/base_emprestimo.html"
        })
        return context


class SearchLivroListView(LivroListView):

    search_value = ''

    def get(self, request: HttpRequest, *args,
            **kwargs) -> HttpResponse:
        self.search_value = request.GET.get('q', '').strip()
        if not self.search_value:
            return redirect('sistema:livros_emprestar')
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


class LivroEmprestarDetailView(DetailView):
    model = Livro
    template_name = "sistema/funcionario/livro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_view_voltar': 'sistema:livros_emprestar',
            'acao_label': "Emprestar",
            'link_acao': 'sistema:emprestar',
            'link_base_html': "global/base_emprestimo.html",
            'title': 'Emprestar'
        })
        return context

    def post(self, request, *args, **kwargs):
        cpf = request.POST.get('cpf', '')
        senha = request.POST.get('senha', '')

        try:
            usuario = self.queryset.get(cpf=cpf, senha=senha)
        except Usuario.DoesNotExist:
            messages.info(request, "Usuario não encontrado")
            return self.get(request, *args, **kwargs)

        emprestimo = Emprestimo()
        emprestimo.user_cpf = cpf
        emprestimo.user_name = usuario.nome_completo
        emprestimo.emprestimo_data = date.today()
        emprestimo.livro_info = self.get_object().pk
        emprestimo.livro_info.emprestado = True
        emprestimo.livro_info.save()
        emprestimo.save()

        messages.info(request, "Livro Emprestado")
        return redirect('sistema:livros_emprestar')


# emprestimo

class EmprestimoListView(ListView):
    model = Emprestimo
    template_name = "sistema/funcionario/emprestimo/emprestimos.html"
    paginate_by = PER_PAGE

    def get_queryset(self):
        return super().get_queryset()\
            .exclude(devolucao_data=None).order_by("devolucao_data")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_emprestimo',
            'link_views_origem': 'sistema:ver_emprestimos',
        })

        return context


class SearchEmprestimo(EmprestimoListView):
    search_value = ''

    def get(self, request: HttpRequest, *args,
            **kwargs) -> HttpResponse:
        self.search_value = request.GET.get('q', '').strip()
        if not self.search_value:
            return redirect('sistema:')
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


class EmprestimoDetaiView(DetailView):
    model = Emprestimo
    template_name = "sistema/funcionario/emprestimo/emprestimo.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_voltar': 'sistema:ver_emprestimos',
            'title': 'Empréstimo',
        })
        return context


class StatusEmprestimoListView(ListView):
    model = Emprestimo
    template_name = "sistema/funcionario/emprestimo/emprestimos.html"
    paginate_by = PER_PAGE

    def get_queryset(self):
        return super().get_queryset()\
            .filter(devolucao_data=None).order_by("emprestimo_data")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_status_emprestimo',
            'link_views_origem': 'sistema:status_emprestimo',
        })
        return context


class StatusEmprestimoDetailView(EmprestimoDetaiView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_voltar': 'sistema:status_emprestimo',
            'link_acao': 'sistema:devolver_livro',
            'acao_label': 'Devolver',
        })
        return context

    def post(self, request, *args, **kwargs):
        emprestimo = get_object_or_404(Emprestimo, pk=kwargs.get("pk"))
        emprestimo.devolucao_data = date.today()
        emprestimo.livro_info.emprestado = False
        emprestimo.livro_info.save()
        emprestimo.save()

        return redirect('sistema:status_emprestimo')


class RenovarEmprestimoListView(StatusEmprestimoListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_revovar_emprestimo',
            'link_views_origem': 'sistema:ver_emprestimo_renovar',
        })
        return context


class RenovarEmprestimoDetailView(EmprestimoDetaiView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_voltar': 'sistema:ver_emprestimo_renovar',
            'link_acao': 'sistema:renovar_emprestimo',
            'acao_label': 'Renovar'
        })
        return context

    def post(self, request, *args, **kwargs):
        emprestimo = get_object_or_404(Emprestimo, pk=kwargs.get("pk"))

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
