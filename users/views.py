from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import UserLoginForm


def sign_in(request):
    if request.method == 'GET':
        form = UserLoginForm
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = authenticate(request, username=phone, password=password)
            if user:
                UserLoginForm(request, user)
                messages.success(request, f'Hi {user.first_name}, welcome back!')
                return reverse_lazy('homepage:home')

        # either form not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})
