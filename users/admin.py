from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as UserAdminDjango
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdminDjango):

    list_display = ('cpf', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('cpf', 'first_name', 'last_name', 'email')
    ordering = ('cpf',)
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
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
