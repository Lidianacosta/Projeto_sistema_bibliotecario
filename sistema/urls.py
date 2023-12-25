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
    path('logout-gerente/', views.logout_funcionario,
         name='logout_funcionario'),

    # Gerente
    path('gerente/solicitacoes/',
         views.SolicitacoesFuncionarioListView.as_view(), name='solicitacoes'),

    path('gerente/<int:pk>/aprovar/',
         views.AprovarFuncionarioDetailView.as_view(), name='ver_aprovar'),

    path('gerente/solicitacoes/<int:pk>/aprovar/',
         views.AprovarFuncionarioDetailView.as_view(), name='aprovar'),

    path('gerente/funcionarios/',
         views.FuncionarioListView.as_view(), name='funcionarios'),

    path('gerente/<int:pk>/excluir/',
         views.ExcluirFuncionarioDetailView.as_view(), name='ver_excluir'),

    path('gerente/funcionarios/<int:pk>/excluir/',
         views.ExcluirFuncionarioDetailView.as_view(), name='excluir'),

    # funcionários


    # empréstimo realizar

    path('funcionario/emprestimo/ver-livros-emprestar/',
         views.LivroListView.as_view(), name='livros_emprestar'),

    path('funcionario/emprestimo/buscar-livro-emprestar/',
         views.SearchLivroListView.as_view(), name='buscar_livros_emprestar'),

    path('funcionario/emprestimo/ver-livro/<int:pk>/realizar-emprestimo/',
         views.LivroEmprestarDetailView.as_view(), name='ver_livro_emprestar'),

    path('funcionario/emprestar/<int:pk>/',
         views.LivroEmprestarDetailView.as_view(), name='emprestar'),

    # status emprestimo

    path("emprestimo/status/",
         views.StatusEmprestimoListView.as_view(), name="status_emprestimo"),

    path("emprestimo/devover/<int:pk>/detail/",
         views.StatusEmprestimoDetailView.as_view(),
         name="ver_status_emprestimo"),

    path("emprestimo/devolver/<int:pk>/",
         views.StatusEmprestimoDetailView.as_view(), name="devolver_livro"),


    # renovar emprestimo

    path("emprestimo/renovar/",
         views.RenovarEmprestimoListView.as_view(),
         name="ver_emprestimo_renovar"),

    path("emprestimo/renovar/<int:pk>/detail/",
         views.RenovarEmprestimoDetailView.as_view(),
         name="ver_revovar_emprestimo"),

    path("emprestimo/<int:pk>/renovar",
         views.RenovarEmprestimoDetailView.as_view(),
         name="renovar_emprestimo"),

    # ver emprestimos

    path("emprestimo/emprestimos/",
         views.EmprestimoListView.as_view(),
         name="ver_emprestimos"),


    path("emprestimo/emprestimos/<int:pk>/detail/",
         views.EmprestimoDetaiView.as_view(),
         name="ver_emprestimo"),

    # excluir livro

    path('funcionario/ver-livros-excluir/',
         views.ExcluirLivroListView.as_view(),
         name='livros_excluir'),

    path('funcionario/ver-livros/<int:pk>/excluir/',
         views.LivroExcluirDetailView.as_view(),
         name='ver_livro_excluir'),

    path('funcionario/<int:pk>/excluir-livro/',
         views.LivroExcluirDetailView.as_view(), name='excluir'),

    # create

    path('cadastra-usuario/',
         views.cadastrar_usuario, name='cadastrar_usuario'),

    path('cadastra-livro/',
         views.cadastrar_livro, name='cadastrar_livro'),

    path('ver-usuarios/', views.UsuarioListView.as_view(),
         name='ver_usuarios'),

    path('ver-usuario/<int:pk>/',
         views.UsuarioDetailView.as_view(), name='ver_usuario'),

    path('delete/usuario/<int:pk>/',
         views.UsuarioDetailView.as_view(), name='deletar_usuario'),
]
