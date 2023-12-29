from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import re
from django.core import validators
from django.utils import timezone
from .managers import UserManager
# Create your models here.

padrao_email = re.compile(
    r'^[a-z0-9._]+@[a-z]+\.([a-z]{3,})(\.[a-z]{2,})?$', flags=re.I
)

padrao_cpf = re.compile(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$')


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'), blank=True, unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
        validators=[
            validators.RegexValidator(
                padrao_email,
                _('Enter a valid email.'),
                _('invalid')
            )
        ]
    )
    cpf = models.CharField(
        _('Cpf'), max_length=14, unique=True,
        help_text='Required. example format: 111.111.111-11',
        error_messages={
            'unique': _("A user with that email already exists."),
        },
        validators=[
            validators.RegexValidator(
                padrao_cpf,
                _('Enter a valid cpf.'),
                _('invalid')
            )
        ]
    )
    first_name = models.CharField(
        _('first name'), max_length=150, blank=True,
        validators=[
            validators.RegexValidator(
                re.compile(r'^[a-zá-ú]+$', flags=re.I),
                _('Enter a valid first_name.'),
                _('invalid')
            )
        ]
    )
    last_name = models.CharField(
        _('last name'), max_length=150, blank=True,
        validators=[
            validators.RegexValidator(
                re.compile(r'^[a-zá-ú]+$', flags=re.I),
                _('Enter a valid last_name.'),
                _('invalid')
            )
        ]
    )
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
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
