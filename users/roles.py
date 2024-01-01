from rolepermissions.roles import AbstractUserRole

EMPRESTAR = 'emprestar'
CADASTRAR_LIVRO = 'cadastrar_livro'
EXCLUIR_LIVRO = 'excluir_livro'
EXCLUIR_USUARIO = 'excluir_usuario'
CRIAR_USUARIO = 'criar_usuario'


class Funcionario(AbstractUserRole):
    available_permissions = {
        EMPRESTAR: True,
        CADASTRAR_LIVRO: True,
        EXCLUIR_LIVRO: True,
        CRIAR_USUARIO: True,
        EXCLUIR_USUARIO: True,
    }


APROVAR_FUNCIONARIO = 'aprovar_funcionario'
EXCLUIR_FUNCIONARIO = 'excluir_funcionario'


class Gerente(AbstractUserRole):
    available_permissions = {
        APROVAR_FUNCIONARIO: True,
        EXCLUIR_FUNCIONARIO: True,
    }
