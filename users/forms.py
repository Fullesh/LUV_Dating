from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput,
        help_text='*<small><em>Ваш номер должен быть в формате: +71234567890</em></small>'
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text='*<small><em>Ваш пароль должен в целом быть</em></small>'
    )

    class Meta:
        model = User
        fields = ('phone', 'password')
