from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from rolepermissions.mixins import HasRoleMixin
from users.models import CustomUser
from sistema.forms import UsuarioForm, FuncionarioForm, GerenteForm
from sistema.models import Livro


class UsuarioFormView(HasRoleMixin, FormView):
    allowed_roles = 'funcionario'
    redirect_to_login = reverse_lazy('sistema:login')
    form_class = UsuarioForm
    success_url = reverse_lazy('sistema:cadastrar_usuario')
    template_name = 'sistema/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'action_form': 'sistema:cadastrar_usuario',
            'memu_link_str': 'memu_funcionario',
        })
        return context


class LivroCreateView(HasRoleMixin, CreateView):
    allowed_roles = 'funcionario'
    redirect_to_login = reverse_lazy('sistema:login')

    model = Livro
    fields = ('livro_id', 'nome', 'autor', 'editora', 'ano')

    success_url = reverse_lazy("sistema:cadastrar_livro")
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
    success_url = reverse_lazy('sistema:cadastrar_funcionario')
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
    success_url = reverse_lazy('sistema:login')
    template_name = 'sistema/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'action_form': 'sistema:cadastrar_gerente',
            'memu_link_str': 'memu_home',

        })
        return context

    def post(self, request, *args, **kwargs):
        exist_gerente = CustomUser.objects.filter(
            groups__name='gerente').exists()
        if exist_gerente:
            messages.info(request, "Só é permitido um gerente")
            return redirect('sistema:login')
        return super().post(request, *args, **kwargs)
