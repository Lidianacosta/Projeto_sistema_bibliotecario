class Gerente():

    def __init__(self, cpf, senha):
        self._cpf = cpf
        self._senha = senha

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
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @senha.getter
    def senha(self):
        return self._senha

    def aprovar(self, solicitacoes: list, funcionarios: list):

        for f in solicitacoes:
            print(f)
            aprovado = input('Aprovado?[Sim|Não] ').lower()

            if aprovado == 'sim':
                funcionarios.append(f)

            print()

        solicitacoes.clear()

    def excluir_funcionario(self, funcionarios, cpf):
        index = None
        for pos, f in enumerate(funcionarios):
            if cpf == f.cpf:
                index = pos

        if index is not None:
            print(funcionarios[index])
            excluir = input(
                'deseja realmente excluir este funcionario?[Sim|Não]').lower()

            if excluir == 'sim':
                del funcionarios[index]
        else:
            print('funcionario não encontrado')
