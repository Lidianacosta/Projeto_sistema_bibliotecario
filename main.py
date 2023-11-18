from src import menus
from src.models.gerente import Gerente
from src.models.sistema import Sistema


def main():

    sistema = Sistema()
    gerente = Gerente()
    funcionarios = []

    while True:
        menus.menu_login()
        escolha = input('Escolha: ')

        if escolha in '13':

            cpf, senha = login()

            if escolha == '1':
                if gerente.autoriza_login(cpf, senha):
                    sistema.sistema_gerente(gerente, funcionarios)
                else:
                    print('login não permitido, informações incoretas')

            else:
                for f in funcionarios:
                    if f.autoriza_login(cpf, senha):
                        sistema.sistema_funcionario(f)
                        break
                else:
                    print('login não permitido, informações incoretas')

        elif escolha == '2':
            sistema.cadastrar_funcionario()
        else:
            if escolha.lower() == 'sair':
                break
            print('opção invalida')


def login():
    cpf = input('login: ')
    senha = input('senha: ')

    return cpf, senha


if __name__ == '__main__':
    # main()
    import src.testes.teste_funcionario
