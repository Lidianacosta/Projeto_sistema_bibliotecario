from django.contrib import admin

from sistema.models import Emprestimo, Funcionario, Gerente, Livro, Usuario

# Register your models here.

admin.site.register(Emprestimo)
admin.site.register(Livro)
admin.site.register(Funcionario)
admin.site.register(Gerente)
admin.site.register(Usuario)