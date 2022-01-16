from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from core.forms import SignUpForm


def homepage(request):
    return render(request, 'core/homepage.html', {'title': 'Home'})


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:home')
    else:
        form = SignUpForm()
        return render(request, 'core/sign_up.html', {'title': 'Sign up', 'form': form})
