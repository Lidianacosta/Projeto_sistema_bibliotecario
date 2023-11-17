from src.models.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome=None, cpf=None, telefone=None, nascimento=None, senha=None, email=None, endereco=None, instituicao=None, idade=None):
        super().__init__(nome, cpf, telefone, nascimento, senha, email)

        self.idade = idade
        self.instituicao = instituicao
        self.endereco = endereco
