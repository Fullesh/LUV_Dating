from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import UserLoginForm
from users.models import User


class UserLoginView(LoginView):
    """
    Контроллер для авторизации пользователя.
    """
    model = User
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('homepage:home')
