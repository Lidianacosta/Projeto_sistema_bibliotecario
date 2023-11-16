from src import menus


def sistema_gerente(gerente, funcionarios):

    solicitacoes = []

    while True:
        menus.menu_gerente()
        escolha = input('escolha: ')

        if escolha == '1':
            gerente.aprovar(solicitacoes)

        elif escolha == '2':
            gerente.excluir_funcionario(funcionarios,
                                        'informação usada para excluir')
        elif escolha == '3':
            break
        else:
            print('opção invalida')


def sistema_funcionario(funcionario):

    livros = []
    usuarios = []

    while True:
        menus.menu_funcionario()
        escolha = input('escolha: ')

        if escolha == '1':
            cadastrar_usuario(usuarios)
        elif escolha == '2':
            cadastrar_livro(livros)
        elif escolha == '3':
            buscar_livro(livros)
        elif escolha == '4':
            funcionario.emprestimo()
        elif escolha == '5':
            remover_livro(livros)
        elif escolha == '6':
            remover_usuario(usuarios)
        elif escolha == '7':
            return
        else:
            print('opção invalida')


def cadastra_funcionarios(funcionarios):
    pass


def cadastrar_usuario(usuarios):
    pass


def remover_usuario(usuarios):
    pass


def cadastrar_livro(livros):
    pass


def remover_livro(livros):
    pass


def buscar_livro(livros):
    pass


def sistema_emprestimo(usuarios, livros):
    emprestimos = []

    while True:

        menus.menu_emprestimos()
        escolha = input('escolha: ')

        if escolha == '1':
            realizar_emprestimo()
        elif escolha == '2':
            visualizar_emprestimos(emprestimos)
        elif escolha == '3':
            status_emprestimo()
        elif escolha == '4':
            renovar_emprestimos()
        elif escolha == '5':
            return
        else:
            print('opção invalida')


def realizar_emprestimo():
    pass


def visualizar_emprestimos(emprestimos):
    pass


def status_emprestimo():
    pass


def renovar_emprestimos():
    pass
