class Pessoa:
    def __init__(self, nome=None, cpf=None, telefone=None, nascimento=None, endereco=None, senha=None, email=None):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._nascimento = nascimento
        self._endereco = endereco
        self._senha = senha
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @nome.getter
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @cpf.getter
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @telefone.getter
    def telefone(self):
        return self._telefone

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @senha.getter
    def senha(self):
        return self._senha

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @email.getter
    def email(self):
        return self._email

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento

    @nascimento.getter
    def nascimento(self):
        return self._nascimento

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @endereco.getter
    def endereco(self):
        return self._endereco

    def autoriza_login(self, cpf, senha):
        if self.cpf == cpf and self.senha == senha:
            return True
        return False
