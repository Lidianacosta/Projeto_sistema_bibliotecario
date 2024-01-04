from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as UserAdminDjango
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class UserAdmin(UserAdminDjango):

    list_display = ('cpf', 'email', 'full_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('cpf', 'full_name', 'email')
    ordering = ('cpf',)
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        (_('Personal info'), {
         'fields': ('full_name', 'email', 'nascimento', 'idade', 'telefone')}),
        (_('Endereço'), {
         'fields': ('estado', 'cidade', 'rua', 'numero')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'password1', 'password2'),
        }),
    )
