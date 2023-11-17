from src import menus
from src import sistema


def main():

    funcionarios = []
    solicitacoes = []
    gerente = []

    while True:
        menus.menu_login()
        escolha = input('Escolha: ')

        if escolha in '13':

            cpf, senha = login()

            if escolha == '1':
                if autoriza_login(gerente, cpf, senha):
                    sistema.sistema_gerente(
                        gerente, funcionarios, solicitacoes)
                else:
                    print('login não permitido, informações incoretas')

            else:
                for f in funcionarios:
                    if autoriza_login(f, cpf, senha):
                        sistema.sistema_funcionario(f)
                        break
                else:
                    print('login não permitido, informações incoretas')

        elif escolha == '2':
            sistema.cadastrar_funcionarios(funcionarios)
        else:
            if escolha.lower() == 'sair':
                break
            print('opção invalida')


def autoriza_login(pessoa, cpf, senha) -> bool:
    if pessoa.cpf == cpf and pessoa.senha == senha:
        return True
    return False


def login():
    cpf = input('login: ')
    senha = input('senha: ')

    return cpf, senha


if __name__ == '__main__':
    main()
