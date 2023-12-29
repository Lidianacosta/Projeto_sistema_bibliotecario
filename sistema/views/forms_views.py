from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib import messages
from sistema.forms import LivroForm, UsuarioForm, FuncionarioForm, GerenteForm
from users.models import User


PERMISSION_GERENTE = [
    ('excluir_funcionario', 'pode excluir funcionario'),
    ('aprovar_funcionario', 'pode aprovar funcionario'),
]


class UsuarioFormView(FormView):
    form_class = UsuarioForm
    success_url = 'sistema:cadastrar_usuario'
    template_name = 'sistema/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'action_form': 'sistema:cadastrar_usuario',
            'caminho_extender': "global/base_funcionario.html",
            'memu_link_str': 'memu_funcionario',
        })
        return context


class LivroFormView(FormView):
    form_class = LivroForm
    success_url = 'sistema:cadastrar_livro'
    template_name = 'sistema/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'action_form': 'sistema:cadastrar_livro',
            'memu_link_str': 'memu_funcionario',
        })
        return context


class FuncionarioFormView(FormView):
    form_class = FuncionarioForm
    success_url = 'sistema:cadastrar_funcionario'
    template_name = 'sistema/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'action_form': 'sistema:cadastrar_funcionario',
            'memu_link_str': 'memu_home',
        })
        return context


class GerenteFormView(FormView):
    form_class = GerenteForm
    success_url = 'sistema:login_gerente'
    template_name = 'sistema/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'action_form': 'sistema:cadastrar_gerente',
            'memu_link_str': 'memu_home',

        })
        return context

    def post(self, request, *args, **kwargs):
        exist = User.objects.filter(
            user_permissions__in=PERMISSION_GERENTE).exists()
        if exist:
            messages.info(request, "Só é permitido um gerente")
            return redirect('sistema:login_gerente')
        return super().post(request, *args, **kwargs)
