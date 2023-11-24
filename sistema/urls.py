from django.urls import path

from . import views

app_name = "sistema"

urlpatterns = [

    path('login/', views.login, name='login'),
    path('cadastrar-funcionario/', views.cadastra_funcionario,
         name='cadastra_funcionario'),

    # Gerente
    path('gerente/solicitacoes/<int:pagina>/',
         views.solicitacoes, name='solicitacoes'),
    path('gerente/solicitacoes/', views.solicitacoes, name='solicitacoes'),

    path('gerente/<int:funcionario_id>/aprovar',
         views.ver_funcionario_aprovar, name='ver_aprovar'),
    path('gerente/solicitacoes/<int:funcionario_id>/aprovar/',
         views.ver_funcionario_aprovar, name='aprovar'),

    path('gerente/funcionarios/<int:pagina>/',
         views.ver_funcionarios, name='funcionarios'),
    path('gerente/funcionarios/', views.ver_funcionarios,
         name='funcionarios'),
    path('gerente/<int:funcionario_id>/excluir/',
         views.funcionario_excluir, name='ver_excluir'),
    path('gerente/funcionarios/<int:funcionario_id>/excluir/',
         views.funcionario_excluir, name='excluir'),

    # funcionários


    # empréstimo realizar


    path('funcionario/emprestimo/ver-livros-emprestar/',
         views.livros_para_empretar, name='livros_emprestar'),
    path('funcionario/emprestimo/ver-livros-emprestar<int:pagina>/',
         views.livros_para_empretar, name='livros_emprestar'),

    path('funcionario/emprestimo/buscar-livro-emprestar/',
         views.buscar_livro_para_emprestar, name='buscar_livros_emprestar'),

    path('funcionario/emprestimo/ver-livro/<int:livro_id>realizar-emprestimo/',
         views.ver_livro_emprestar, name='ver_livro_emprestar'),

    path('funcionario/<int:livro_id>/emprestar/',
         views.realizar_emprestimo, name='emprestar'),

    # ver emprestimos

    path("emprestimo/emprestimos",
         views.emprestimos, name="ver_emprestimos"),

    path("emprestimo/buscar-emprestimos",
         views.buscar_emprestimos, name="busca_emprestimos"),


    #     path("funcionario/emprestimo/emprestimos",
    #          views.ver_emprestimo, name="ver_emprestimo"),

    #     path("funcionario/emprestimo/devolver<int:emprestimo_id",
    #          views.devolver_livro, name="devolver"),



    # excluir livro
    path('funcionario/ver-livros-excluir/<int:pagina>/', views.livros_para_excluir,
         name='livros_excluir'),

    path('funcionario/ver-livros-excluir/', views.livros_para_excluir,
         name='livros_excluir'),


    path('funcionario/ver-livros/<int:livro_id>/excluir/',
         views.ver_livro_excluir, name='ver_livro_excluir'),

    path('funcionario/buscar-livro-emprestar/',
         views.buscar_livro_para_excluir, name='buscar_livros_excluir'),

    path('funcionario/excluir-livro/',
         views.excluir_livro, name='excluir'),


    # create

    path('cadastra-usuario/',
         views.cadastrar_usuario, name='cadastrar_usuario'),

    path('cadastra-livro/',
         views.cadastrar_livro, name='cadastrar_livro'),

]
