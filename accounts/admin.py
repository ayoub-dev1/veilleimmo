from django.contrib import admin
from django import forms

from django.contrib.auth.models import Group 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import  User
from .forms import ChangeForm, UserCreationForm


class UserAadmin(BaseUserAdmin):
    form     = ChangeForm
    add_form = UserCreationForm

    list_display = ('username','email', 'is_admin', 'is_active')
    list_filter  = ('is_admin',)

    fieldsets = (
        (None, {'fields':('username', 'email', 'password')}),
        ('Permissions', {'fields':('is_admin', 'is_staff','is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields': ('username', 'email', 'passwors1', 'password2')}
            ),
    )


    search_fields = ('username', 'email')
    ordering      = ('username','email')
    filter_horizontal = ()


admin.site.register(User, BaseUserAdmin)
admin.site.unregister(Group)