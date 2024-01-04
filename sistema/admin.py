from django.contrib import admin
from .models import Emprestimo, Funcionario, Livro, Usuario

# Register your models here.


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'livro_id', 'nome', 'ano', 'emprestado')
    list_display_links = ('nome',)
    search_fields = ('id', 'livro_id', 'nome', 'ano', 'emprestado')
    list_per_page = 10
    ordering = ('-id',)
    list_filter = ('emprestado',)
    readonly_fields = ('emprestado',)


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_cpf', 'livro_info')
    list_display_links = ('user_name', 'user_cpf', 'livro_info')
    search_fields = ('id', 'user_name', 'user_cpf', 'livro_info')
    list_per_page = 10
    ordering = ('-id',)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_filter = ('habilitado',)
    readonly_fields = ('habilitado',)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
