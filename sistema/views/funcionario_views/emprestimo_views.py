from datetime import date
from rolepermissions.mixins import HasRoleMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from sistema.models import Emprestimo, Livro, Usuario

GRUPO = 'funcionario'
LOGIN_URL = 'sistema:login_funcionario'

PER_PAGE = 4


class LivroListView(HasRoleMixin, ListView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
    model = Livro
    paginate_by = PER_PAGE
    template_name = "sistema/funcionario/livros.html"

    def get_queryset(self):
        return super().get_queryset().filter(emprestado=False).order_by("nome")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:emprestar',
            'busca_action': 'sistema:buscar_livros_emprestar',
            'memu_link_str': 'memu_emprestimo',
        })
        return context


class LivroEmprestarDetailView(HasRoleMixin, DetailView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
    model = Livro
    template_name = "sistema/funcionario/livro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_view_voltar': 'sistema:livros_emprestar',
            'acao_label': "Emprestar",
            'link_acao': 'sistema:emprestar',
            'title': 'Emprestar'
        })
        return context

    def post(self, request, *args, **kwargs):
        cpf = request.POST.get('cpf', '')
        senha = request.POST.get('senha', '')

        try:
            usuario = Usuario.objects.get(cpf=cpf, senha=senha)
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

        return redirect('sistema:livros_emprestar')


# emprestimo

class EmprestimoListView(HasRoleMixin, ListView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
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
            'busca_action': 'sistema:busca_emprestimos',
            'memu_link_str': 'memu_emprestimo',
        })

        return context


class EmprestimoDetaiView(HasRoleMixin, DetailView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
    model = Emprestimo
    template_name = "sistema/funcionario/emprestimo/emprestimo.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_voltar': 'sistema:ver_emprestimos',
            'title': 'Empréstimo',
        })
        return context


class StatusEmprestimoListView(HasRoleMixin, ListView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
    model = Emprestimo
    template_name = "sistema/funcionario/emprestimo/emprestimos.html"
    paginate_by = PER_PAGE

    def get_queryset(self):
        return super().get_queryset()\
            .filter(devolucao_data=None).order_by("emprestimo_data")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'link_views_acao': 'sistema:devolver_livro',
            'busca_action': 'sistema:buscar_status_emprestimo',
            'memu_link_str': 'memu_emprestimo',
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
            'link_views_acao': 'sistema:renovar_emprestimo',
            'link_busca': 'sistema:buscar_emprestimo_renovar',
            'memu_link_str': 'memu_emprestimo',
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
        emprestimo = self.get_object()

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
