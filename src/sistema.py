from src import menus
from src.models.funcionario import Funcionario


def sistema_gerente(gerente, funcionarios, solicitacoes):

    while True:
        menus.menu_gerente()
        escolha = input('escolha: ')

        if escolha == '1':
            gerente.aprovar(solicitacoes, funcionarios)

        elif escolha == '2':
            print('listando funcionarios cadastrados no sistema:')
            for f in funcionarios:
                print(f)
            cpf = input('cpf: ')
            gerente.excluir_funcionario(funcionarios, cpf)
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
            sistema_emprestimo(usuarios, livros)
        elif escolha == '5':
            remover_livro(livros)
        elif escolha == '6':
            remover_usuario(usuarios)
        elif escolha == '7':
            return
        else:
            print('opção invalida')


def cadastrar_funcionarios(funcionarios: list):
    funcionario = Funcionario()

    funcionario.nome = input('nome: ')
    funcionario.cpf = input('cpf: ')
    funcionario.telefone = input('telefone: ')
    funcionario.nascimento = input('nascimento: ')
    funcionario.email = input('email: ')
    estado = input('estado: ')
    cidade = input('cidade: ')

    funcionario.senha = input('senha: ')

    funcionarios.append(funcionario)


def cadastrar_usuario(usuarios):
    pass


def remover_usuario(usuarios):
    pass


def cadastrar_livro(livros: list):
    print('complete os campos de casdastros')
    livro = {}
    livro['nome'] = input('nome:')
    livro['id'] = int(input('id:'))
    livro['autor'] = input('autor:')
    livro['editora'] = input('editora:')
    livro['ano'] = int(input('ano:'))

    livros.append(livro)


def remover_livro(livros: list):
    index_excluir = None
    print('Qual livro deseja remover')
    if not buscar_livro(livros):
        return

    excluir_id = int(input('informe o id do livro que deseja remover: '))

    for pos, livro in enumerate(livros):
        if excluir_id == livro['id']:
            index_excluir = pos

    if index_excluir is None:
        print('livro não encontrado')
        return

    livro_excluir = livros.pop(index_excluir)
    print(
        f'Id: {livro_excluir["id"]}',
        f'Nome: {livro_excluir["nome"]}',
        f'Autor: {livro_excluir["autor"]}',
        f'Editora: {livro_excluir["editora"]}',
        f'Ano: {livro_excluir["ano"]}',
        sep='\n'
    )
    livro_excluir['motivo da exclusão'] = input(
        'innforme o motivo pela remocão do livro: ')

    # salvar em um arquivo livro_excluir


def buscar_livro(livros: list) -> bool:
    info = input('informacão do livro deseja buscar:')
    livros_encontrados = []

    for livro in livros:
        if info in livro.values():
            livros_encontrados.append(livro)

    if not livros_encontrados:
        print('Nenhum livro encontrado')
        return False

    print('livros encontrados:')

    for livro in livros_encontrados:
        print()
        print(
            f'Id: {livro["id"]}',
            f'Nome: {livro["nome"]}',
            f'Autor: {livro["autor"]}',
            f'Editora: {livro["editora"]}',
            f'Ano: {livro["ano"]}',
            sep='\n'
        )

    return True


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
