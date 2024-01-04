from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from rolepermissions.mixins import HasRoleMixin
from sistema.models import Usuario, Emprestimo
from .emprestimo_views import PER_PAGE, LivroListView, LivroEmprestarDetailView

LOGIN_URL = 'sistema:login'


class ExcluirLivroListView(LivroListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:excluir_livro',
            'link_busca': 'sistema:buscar_livros_excluir',
            'memu_link_str': 'memu_funcionario',
        })
        return context


class LivroExcluirDetailView(LivroEmprestarDetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_view_voltar': 'sistema:livros_excluir',
            'acao_label': "Excluir Livro",
            'link_acao': 'sistema:excluir_livro',
        })
        return context

    def post(self, request, *args, **kwargs):
        livro = self.get_object()
        livro.delete()
        return redirect('sistema:livros_excluir')


class UsuarioListView(HasRoleMixin, ListView):
    allowed_roles = 'funcionario'
    redirect_to_login = LOGIN_URL
    model = Usuario
    template_name = 'sistema/gerente/funcionarios.html'
    paginate_by = PER_PAGE

    def get_queryset(self):
        cpfs_with_loans = {
            e.user_cpf
            for e in Emprestimo.objects.filter(devolucao_data=None)
        }
        return super().get_queryset()\
            .exclude(cpf__in=cpfs_with_loans).order_by("nome_completo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:deletar_usuario',
            'tabela_titulo': 'Usuários',
            'busca_action': 'sistema:busca_usuarios',
            'memu_link_str': 'memu_funcionario',
        })
        return context


class UsuarioDetailView(HasRoleMixin, DetailView):
    allowed_roles = 'funcionario'
    redirect_to_login = LOGIN_URL
    model = Usuario
    template_name = 'sistema/funcionario/usuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_template_voltar': "sistema:ver_usuarios",
            'acao_label': "Excluir",
            'acao_link': "sistema:deletar_usuario",
        })
        return context

    def post(self, request, *args, **kwargs):
        usuario = self.get_object()
        usuario.delete()
        return redirect('sistema:ver_usuarios')
