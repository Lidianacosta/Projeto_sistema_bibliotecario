def menu_login():
    print('\n', '=' * 35, sep='')
    print(f'{" Menu inicial" :^35}')
    print(' 1 - login gerente\n 2 - cadastro funcionário\n 3 - login')
    print('=' * 35, '\n')


def menu_gerente():
    print('\n', '=' * 35, sep='')
    print(f'{" Menu Do Gerente" :^35}')
    print(' 1 - Ver funcionários esperando aprovação',
          ' 2 - Excluir Funcionario',
          ' 3 - logout',
          sep='\n'
          )
    print('=' * 35, '\n')


def menu_funcionario():
    print('\n', '=' * 35, sep='')
    print(f'{" Menu Do Funcionário" :^35}')
    print(' 1 - cadastrar usuário',
          ' 2 - cadastrar livro',
          ' 3 - buscar livro',
          ' 4 - empréstimos',
          ' 5 - remover livro',
          ' 6 - remover usuário',
          ' 7 - logout',
          sep='\n'
          )
    print('=' * 35, '\n')


def menu_emprestimos():
    print('\n', '=' * 35, sep='')
    print(f'{" Menu empréstimos" :^35}')
    print(' 1 - Realizar empréstimos',
          ' 2 - visualizar empréstimos',
          ' 3 - status do empréstimo',
          ' 4 - renovar empréstimos',
          ' 5 - voltar',
          sep='\n'
          )
    print('=' * 35, '\n')
