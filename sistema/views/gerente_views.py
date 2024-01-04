from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from rolepermissions.roles import assign_role
from rolepermissions.mixins import HasRoleMixin
from sistema.models import Funcionario
from .funcionario_views.emprestimo_views import PER_PAGE

GRUPO = 'gerente'
LOGIN_URL = 'sistema:login'


class SolicitacoesFuncionarioListView(HasRoleMixin, ListView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
    model = Funcionario
    template_name = "sistema/gerente/funcionarios.html"
    paginate_by = PER_PAGE

    def get_queryset(self):
        return super().get_queryset()\
            .filter(habilitado=False).order_by("nome_completo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:aprovar',
            'tabela_titulo': 'Funcionários',
            'busca_action': 'sistema:solicitacoes',
            'memu_link_str': 'memu_gerente',
        })
        return context


class AprovarFuncionarioDetailView(HasRoleMixin, DetailView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
    model = Funcionario
    template_name = 'sistema/gerente/funcionario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_template_voltar': "sistema:solicitacoes",
            'acao_label': "Aprovar",
            'acao_link': "sistema:aprovar",
        })
        return context

    def post(self, request, *args, **kwargs):
        funcionario = self.get_object()
        assign_role(funcionario.user, 'funcionario')
        funcionario.user.save()
        funcionario.habilitado = True
        funcionario.save()

        return redirect('sistema:solicitacoes')


class FuncionarioListView(PermissionRequiredMixin, ListView):
    allowed_roles = GRUPO
    redirect_to_login = LOGIN_URL
    model = Funcionario
    template_name = "sistema/gerente/funcionarios.html"
    paginate_by = PER_PAGE

    def get_queryset(self):
        return super().get_queryset()\
            .filter(habilitado=True).order_by("nome_completo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:excluir_funcionario',
            'tabela_titulo': 'Funcionários',
            'busca_action': 'sistema:busca_funcionarios',
            'memu_link_str': 'memu_gerente',
        })
        return context


class ExcluirFuncionarioDetailView(AprovarFuncionarioDetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_template_voltar': "sistema:funcionarios",
            'acao_label': "Excluir",
            'acao_link': "sistema:excluir_funcionario"
        })
        return context

    def post(self, request, *args, **kwargs):
        funcionaro = self.get_object()
        funcionaro.delete()

        return redirect('sistema:funcionarios')
