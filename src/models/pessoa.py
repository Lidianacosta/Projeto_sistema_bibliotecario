class Pessoa:
    def __init__(self, nome, cpf, telefone, nascimento, endereco, senha, email) -> None:
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._nascimento = nascimento
        self._endereco = endereco
        self._senha = senha
        self._email = email

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome) -> None:
        self._nome = nome

    @nome.getter
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf) -> None:
        self._cpf = cpf

    @cpf.getter
    def cpf(self) -> str:
        return self._cpf

    @property
    def telefone(self) -> int:
        return self._telefone

    @telefone.setter
    def telefone(self, telefone) -> None:
        self._telefone = telefone

    @telefone.getter
    def telefone(self) -> int:
        return self._telefone

    @property
    def senha(self) -> str:
        return self._senha

    @senha.setter
    def senha(self, senha) -> None:
        self._senha = senha

    @senha.getter
    def senha(self) -> str:
        return self._senha

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email) -> None:
        self._email = email

    @email.getter
    def email(self) -> str:
        return self._email

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento) -> None:
        self._nascimento = nascimento

    @nascimento.getter
    def nascimento(self) -> int:
        return self._nascimento
