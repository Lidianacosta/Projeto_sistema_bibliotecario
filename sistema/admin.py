from django.contrib import admin

from sistema.models import Emprestimo, Funcionario, Livro, Usuario

# Register your models here.

admin.site.register(Emprestimo)
admin.site.register(Livro)
admin.site.register(Funcionario)
admin.site.register(Usuario)
