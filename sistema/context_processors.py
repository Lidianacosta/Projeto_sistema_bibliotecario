
def menu_link(request):
    menu = {
        'memu_emprestimo': {
            'Realizar Empréstimos': 'sistema:livros_emprestar',
            'Visualizar Empréstimos': 'sistema:ver_emprestimos',
            'Status dos Empréstimos': 'sistema:status_emprestimo',
            'Renovar Empréstimos': 'sistema:ver_emprestimo_renovar',
            'Voltar': 'sistema:cadastrar_usuario'
        },
        'memu_funcionario': {
            'Cadastrar Usuário': 'sistema:cadastrar_usuario',
            'cadastrar Livro': 'sistema:cadastrar_livro',
            'Empréstimos': 'sistema:livros_emprestar',
            'Remover Livro': 'sistema:livros_excluir',
            'Remover Usuário': 'sistema:ver_usuarios',
            'Logout': 'sistema:logout',
        },
        'memu_gerente': {
            'Solicitações': 'sistema:solicitacoes',
            'Funcionários': 'sistema:funcionarios',
            'Logout': 'sistema:logout',
        },
        'memu_home': {
            'Login': 'sistema:login',
            'Cadastrar Funcionário': 'sistema:cadastrar_funcionario',
        },
    }
    return {'menu_link': menu}
