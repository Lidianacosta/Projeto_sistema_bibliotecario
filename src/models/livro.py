class Livro:
    def __init__(self, nome, autor, idd, ano, editora) -> None:
        self._nome = nome
        self._autor = autor
        self._idd = idd
        self._ano = ano
        self._editora = editora

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
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, autor) -> None:
        self._autor = autor

    @autor.getter
    def autor(self) -> str:
        return self._autor

    @property
    def idd(self) -> int:
        return self._numero

    @idd.setter
    def idd(self, idd) -> None:
        self._numero = idd

    @idd.getter
    def idd(self) -> int:
        return self._numero

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, ano) -> None:
        self._ano = ano

    @ano.getter
    def ano(self) -> int:
        return self._ano

    @property
    def editora(self) -> str:
        return self._editora

    @editora.setter
    def editora(self, editora) -> None:
        self._editora = editora

    @editora.getter
    def editora(self) -> str:
        return self._editora
