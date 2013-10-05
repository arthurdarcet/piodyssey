from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.db import models

from .models import User


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    password1 = forms.CharField(label='New password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmation', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False

    def clean_password(self):
        return self.initial.get('password', None)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        if self.cleaned_data['password1']:
            user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserAdmin(DjUserAdmin):
    form = UserChangeForm
    add_form = UserChangeForm

    list_display = ('email', 'first_name', 'last_name', 'team', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'team', 'date_of_birth', 'phone', 'facebook', 'contact_method')}),
        ('Parents', {'fields': ('parents_phone', 'parents_email')}),
        ('Permissions', {'fields': ('is_staff',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
