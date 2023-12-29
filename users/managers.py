from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, cpf, email, password, **extra_fields):
        now = timezone.now()

        if not cpf:
            raise ValueError('The given cpf must be set')

        email = self.normalize_email(email)
        user = self.model(
            cpf=cpf, email=email, last_login=now,
            date_joined=now, **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cpf, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(cpf, email, password, **extra_fields)

    def create_superuser(self, cpf, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(cpf, email, password, **extra_fields)
