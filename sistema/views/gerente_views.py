from django.shortcuts import redirect
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView, DetailView
from sistema.models import Funcionario
from .funcionario_views.emprestimo_views import PER_PAGE


class SolicitacoesFuncionarioListView(ListView):
    model = Funcionario
    template_name = "sistema/gerente/funcionarios.html"
    paginate_by = PER_PAGE

    def get_queryset(self):
        return super().get_queryset()\
            .filter(habilitado=False).order_by("nome_completo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_aprovar',
            'tabela_titulo': 'Funcionários',
            'busca_action': 'sistema:solicitacoes',
            'memu_link_str': 'memu_gerente',
        })
        return context


class AprovarFuncionarioDetailView(DetailView):
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
        content_type = ContentType.objects.get_for_model(Funcionario)
        permission = Permission.objects.filter(content_type=content_type)

        funcionario.user.user_permissions.set(list(permission))
        funcionario.user.save()
        funcionario.habilitado = True
        funcionario.save()

        return redirect('sistema:solicitacoes')


class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "sistema/gerente/funcionarios.html"
    paginate_by = PER_PAGE

    def get_queryset(self):
        return super().get_queryset()\
            .filter(habilitado=True).order_by("nome_completo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_excluir',
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
            'acao_link': "sistema:excluir"
        })
        return context

    def post(self, request, *args, **kwargs):
        funcionaro = self.get_object()
        funcionaro.delete()

        return redirect('sistema:funcionarios')
