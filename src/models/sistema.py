from src import menus
from src.models.funcionario import Funcionario


class Sistema:

    def __init__(self) -> None:
        self._livros_removidos = []
        self._solicitacoes = []
        self._emprestimos = []
        self._usuarios = []
        self._livros = []

    def sistema_gerente(self, gerente, funcionarios):

        while True:
            menus.menu_gerente()
            escolha = input('escolha: ')

            if escolha == '1':
                gerente.aprovar(self._solicitacoes, funcionarios)

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

    def cadastrar_funcionario(self):
        funcionario = Funcionario()

        funcionario.nome = input('nome: ')
        funcionario.cpf = input('cpf: ')
        funcionario.telefone = input('telefone: ')
        funcionario.nascimento = input('nascimento: ')
        funcionario.email = input('email: ')
        funcionario.estado = input('estado: ')
        funcionario.cidade = input('cidade: ')

        funcionario.senha = input('senha: ')

        self._solicitacoes.append(funcionario)

    def sistema_funcionario(self, funcionario):

        while True:
            menus.menu_funcionario()
            escolha = input('escolha: ')

            if escolha == '1':
                funcionario.cadastrar_usuario(self._usuarios)
            elif escolha == '2':
                funcionario.cadastrar_livro(self._livros)
            elif escolha == '3':
                funcionario.buscar_livro(self._livros)
            elif escolha == '4':
                self.sistema_emprestimo(funcionario)
            elif escolha == '5':
                funcionario.remover_livro(self._livros, self._livros_removidos)
            elif escolha == '6':
                funcionario.remover_usuario(self._usuarios)
            elif escolha == '7':
                return
            else:
                print('opção invalida')

    def sistema_emprestimo(self, funcionario):
        while True:

            menus.menu_emprestimos()
            escolha = input('escolha: ')

            if escolha == '1':
                funcionario.realizar_emprestimo(
                    self._livros, self._usuarios, self._emprestimos)
            elif escolha == '2':
                funcionario.visualizar_emprestimos(self._emprestimos)
            elif escolha == '3':
                funcionario.status_emprestimo(self._emprestimos)
            elif escolha == '4':
                funcionario.renovar_emprestimos(
                    self._emprestimos, self._usuarios)
            elif escolha == '5':
                return
            else:
                print('opção invalida')
