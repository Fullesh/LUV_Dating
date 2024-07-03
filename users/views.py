from django.contrib import messages
from django.contrib.auth.views import LoginView

from users.forms import UserLoginForm
from users.models import User


class UserLoginView(LoginView):
    """
    Контроллер для авторизации пользователя.
    """
    model = User
    redirect_authenticated_user = True
    context_object_name = 'user'
    authentication_form = UserLoginForm
    template_name = 'users/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Неверное имя пользователя или пароль')
        return self.render_to_response(self.get_context_data(form=form))

