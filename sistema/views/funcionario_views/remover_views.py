from django.shortcuts import redirect
from sistema.models import Usuario, Emprestimo
from django.views.generic import ListView, DetailView
from .emprestimo_views import PER_PAGE, LivroListView, LivroEmprestarDetailView


class ExcluirLivroListView(LivroListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_livro_excluir',
            'link_views_origem': "sistema:livros_excluir",
            'link_busca': 'sistema:buscar_livros_excluir',
            'link_base_html': "global/base_funcionario.html"
        })
        return context


class LivroExcluirDetailView(LivroEmprestarDetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_view_voltar': 'sistema:livros_excluir',
            'acao_label': "Excluir Livro",
            'link_acao': 'sistema:excluir',
            'link_base_html': "global/base_funcionario.html",
        })
        return context

    def post(self, request, *args, **kwargs):
        livro = self.get_object()
        livro.delete()
        return redirect('sistema:livros_excluir')


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'sistema/gerente/funcionarios.html'
    paginate_by = PER_PAGE

    def get_queryset(self):
        cpfs_with_loans = {
            e.user_cpf
            for e in Emprestimo.objects.filter(devolucao_data=None)
        }
        return super().get_queryset().exclude(cpf__in=cpfs_with_loans).order_by("nome_completo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'link_views_acao': 'sistema:ver_usuario',
            'link_base_html': "global/base_funcionario.html",
            'tabela_titulo': 'Usuários',
            'busca_action': 'sistema:busca_usuarios',
        })
        return context


class UsuarioDetailView(DetailView):
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
