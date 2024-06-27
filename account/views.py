from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import authenticate, login, logout

from room.models import Room


# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():

            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user:
                login(request, user)
                return redirect('account:home')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('account:home')


def home(request):
    return render(request, 'home.html')
