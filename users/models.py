import re
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.utils import timezone
from sistema.validator import validate_nascimento
from .managers import UserManager

# Create your models here.

PADRAO_EMAIL = r'^[a-z0-9._]+@[a-z]+\.([a-z]{3,})(\.[a-z]{2,})?$'
PADRAO_CPF = r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$'
PADRAO_TELEFONE = r'^\(?[0-9]{2}\)?[\s]?[9]?[0-9]{4}[-]?[0-9]{4}$'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'), blank=True, unique=True, null=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
        validators=[
            validators.RegexValidator(
                re.compile(PADRAO_EMAIL, re.I),
                _('Enter a valid email.'),
                _('invalid')
            )
        ]
    )
    cpf = models.CharField(
        _('Cpf'), max_length=14, unique=True,
        help_text='Required. example format: 111.111.111-11',
        error_messages={
            'unique': _("A user with that cpf already exists."),
        },
        validators=[
            validators.RegexValidator(
                re.compile(PADRAO_CPF),
                _('Enter a valid cpf.'),
                _('invalid')
            )
        ]
    )
    full_name = models.CharField(
        _('full name'), max_length=150, blank=True, null=True,
        validators=[
            validators.RegexValidator(
                re.compile(r'^[a-zá-ú\s]+$', flags=re.I),
                _('Enter a valid full_name.'),
                _('invalid')
            )
        ]
    )
    telefone = models.CharField(
        max_length=50, blank=True, unique=True, null=True,
        validators=[
            validators.RegexValidator(
                re.compile(PADRAO_TELEFONE),
                _('Enter a valid telefone.'),
                _('invalid')
            )
        ]
    )
    nascimento = models.DateField(
        default=None, null=True, blank=True,
        validators=[validate_nascimento]
    )
    idade = models.PositiveIntegerField(default=None, blank=True, null=True,)
    estado = models.CharField(max_length=2, default='', blank=True, null=True,)
    cidade = models.CharField(
        max_length=50, default='', blank=True, null=True,)
    rua = models.CharField(max_length=50, default='', blank=True, null=True,)
    numero = models.PositiveIntegerField(default=None, blank=True, null=True,)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('custom user')
        verbose_name_plural = _('custom users')

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self) -> str:
        return '%s' % self.full_name if self.full_name else self.cpf

    def save(self, *args, **kwargs):
        if self.nascimento:
            self.idade = (date.today() - self.nascimento).days // 365
        super().save(*args, **kwargs)
