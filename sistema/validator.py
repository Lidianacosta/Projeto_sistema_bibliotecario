import re
from datetime import date
from django.core.exceptions import ValidationError

padrao_cpf = re.compile(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$')
padrao_telefone = re.compile(r'^\(?[0-9]{2}\)?[\s]?[9]?[0-9]{4}[-]?[0-9]{4}$')
padrao_email = re.compile(
    r'^[a-z0-9._]+@[a-z]+\.([a-z]{3,})(\.[a-z]{2,})?$', flags=re.I)
padrao_nome = re.compile(r'^[a-zá-ú\s]*$', flags=re.I)


def validate_name(nome):
    if not padrao_nome.search(nome):
        raise ValidationError(
            message='Nome inválido',
            code='invalid'
        )


def validate_telefone(telefone):
    if not padrao_telefone.search(telefone):
        raise ValidationError(
            message='Telefone inválido',
            code='invalid'
        )


def validate_cpf(cpf):
    if not padrao_cpf.search(cpf):
        raise ValidationError(
            message='Cpf inválido',
            code='invalid'
        )


def validate_email(email):
    if not padrao_email.search(email):
        raise ValidationError(
            message='Email inválido',
            code='invalid'
        )


def validate_nascimento(nascimento):
    idade = (date.today() - nascimento).days // 365
    if idade < 18:
        raise ValidationError(
            message='Menor de Idade',
            code='invalid'
        )
