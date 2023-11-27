from django import template
from datetime import date


register = template.Library()


@register.filter('status')
def calcula_status(emprestimo):

    if emprestimo.devolucao_data:
        return 'entregue'

    dias_emprestado = (date.today() - emprestimo.emprestimo_data).days

    if dias_emprestado <= 8:
        return 'ativo'

    return 'atrasado'
