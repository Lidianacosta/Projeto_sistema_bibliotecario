from django.urls import path

from . import views

app_name = "sistema"

urlpatterns = [

    path('login-gerente/', views.login_gerente, name='login_gerente'),
    path('login-funcionario/',
         views.login_funcionario, name='login_funcionario'),
    path('cadastrar-funcionario/', views.cadastrar_funcionario,
         name='cadastrar_funcionario'),
    path('cadastrar-gerente/', views.cadastrar_gerente,
         name='cadastrar_gerente'),
    path('logout-gerente/', views.logout_gerente, name='logout_gerente'),
    path('logout-gerente/', views.logout_funcionario, name='logout_funcionario'),

    # Gerente
    path('gerente/solicitacoes/<int:pagina>/page',
         views.solicitacoes, name='solicitacoes'),
    path('gerente/solicitacoes/', views.solicitacoes, name='solicitacoes'),

    path('gerente/<int:funcionario_id>/aprovar/',
         views.ver_funcionario_aprovar, name='ver_aprovar'),

    path('gerente/solicitacoes/<int:funcionario_id>/aprovar/',
         views.aprovar, name='aprovar'),

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

    path('funcionario/emprestimo/ver-livros-emprestar/<int:pagina>/',
         views.livros_para_empretar, name='livros_emprestar'),

    path('funcionario/emprestimo/buscar-livro-emprestar/<int:pagina>/',
         views.buscar_livro_para_emprestar, name='buscar_livros_emprestar'),

    path('funcionario/emprestimo/buscar-livro-emprestar/',
         views.buscar_livro_para_emprestar, name='buscar_livros_emprestar'),

    path('funcionario/emprestimo/ver-livro/<int:livro_id>/realizar-emprestimo/',
         views.ver_livro_emprestar, name='ver_livro_emprestar'),

    path('funcionario/emprestar/<int:livro_id>/',
         views.realizar_emprestimo, name='emprestar'),



    # status emprestimo

    path("emprestimo/status/",
         views.status_emprestimo, name="status_emprestimo"),

    path("emprestimo/status/<int:pagina>/",
         views.status_emprestimo, name="status_emprestimo"),

    path("emprestimo/buscar-emprestimos-devolver/<int:pagina>/",
         views.buscar_emprestimos, name="buscar_status_emprestimo"),

    path("emprestimo/buscar-emprestimos-devolver/",
         views.buscar_emprestimos, name="buscar_status_emprestimo"),

    path("emprestimo/devover/<int:emprestimo_id>/detail/",
         views.ver_status_emprestimo, name="ver_status_emprestimo"),

    path("emprestimo/devolver/<int:emprestimo_id>/",
         views.devolver_livro, name="devolver_livro"),


    # renovar emprestimo

    path("emprestimo/renovar/",
         views.ver_emprestimo_renovar, name="ver_emprestimo_renovar"),

    path("emprestimo/renovar/<int:pagina>/",
         views.ver_emprestimo_renovar, name="ver_emprestimo_renovar"),

    path("emprestimo/buscar-emprestimos-renovar/<int:pagina>/",
         views.buscar_emprestimos, name="buscar_emprestimo_renovar"),

    path("emprestimo/buscar-emprestimos-renovar/",
         views.buscar_emprestimos, name="buscar_emprestimo_renovar"),

    path("emprestimo/renovar/<int:emprestimo_id>/detail/",
         views.ver_revovar_emprestimo, name="ver_revovar_emprestimo"),

    path("emprestimo/<int:emprestimo_id>/renovar",
         views.renovar_emprestimo, name="renovar_emprestimo"),

    # ver emprestimos

    path("emprestimo/emprestimos/",
         views.emprestimos, name="ver_emprestimos"),

    path("emprestimo/emprestimos/<int:pagina>/",
         views.emprestimos, name="ver_emprestimos"),

    path("emprestimo/buscar-emprestimos/<int:pagina>/",
         views.buscar_emprestimos, name="busca_emprestimos"),

    path("emprestimo/buscar-emprestimos/",
         views.buscar_emprestimos, name="busca_emprestimos"),


    path("emprestimo/emprestimos/<int:emprestimo_id>/detail/",
         views.ver_emprestimo, name="ver_emprestimo"),


    # excluir livro
    path('funcionario/ver-livros-excluir/<int:pagina>/',
         views.livros_para_excluir, name='livros_excluir'),

    path('funcionario/ver-livros-excluir/',
         views.livros_para_excluir, name='livros_excluir'),


    path('funcionario/buscar-livro-emprestar/<int:pagina>/',
         views.buscar_livro_para_excluir, name='buscar_livros_excluir'),

    path('funcionario/buscar-livro-emprestar/',
         views.buscar_livro_para_excluir, name='buscar_livros_excluir'),

    path('funcionario/ver-livros/<int:livro_id>/excluir/',
         views.ver_livro_excluir, name='ver_livro_excluir'),

    path('funcionario/<int:livro_id>/excluir-livro/',
         views.excluir_livro, name='excluir'),


    # create

    path('cadastra-usuario/',
         views.cadastrar_usuario, name='cadastrar_usuario'),

    path('cadastra-livro/',
         views.cadastrar_livro, name='cadastrar_livro'),

    path('ver-usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('ver-usuarios/<int:pagina>/', views.ver_usuarios, name='ver_usuarios'),
    path('ver-usuario/<int:usuario_id>/',
         views.ver_usuario, name='ver_usuario'),
    path('delete/usuario/<int:usuario_id>/',
         views.deletar_usuario, name='deletar_usuario'),
]
