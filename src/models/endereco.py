class Endereco:
    def __init__(self, cidade, rua, numero, estado) -> None:
        self._cidade = cidade
        self._rua = rua
        self._numero = numero
        self._estado = estado

    @property
    def cidade(self) -> str:
        return self._cidade

    @cidade.setter
    def cidade(self, cidade) -> None:
        self._cidade = cidade

    @cidade.getter
    def cidade(self) -> str:
        return self._cidade

    @property
    def rua(self) -> str:
        return self._rua

    @rua.setter
    def rua(self, rua) -> None:
        self._rua = rua

    @rua.getter
    def rua(self) -> str:
        return self._rua

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, numero) -> None:
        self._numero = numero

    @numero.getter
    def numero(self) -> int:
        return self._numero

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, estado) -> None:
        self._estado = estado

    @estado.getter
    def estado(self) -> str:
        return self._estado
