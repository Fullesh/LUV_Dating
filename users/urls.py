from django.urls import path

from users.apps import UsersConfig
from users.views import sign_in

app_name = UsersConfig.name
urlpatterns = [
    path('login/', sign_in, name='login')
]
