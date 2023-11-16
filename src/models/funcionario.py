from src.models.pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome=..., cpf=..., telefone=..., nascimento=..., endereco=..., senha=..., email=...):
        super().__init__(nome, cpf, telefone, nascimento, endereco, senha, email)
