from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CustomForm
from .models import CustomUserModel


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:            
            login(request, user)
            return redirect('home')
        else:
            return redirect('User credential wrong please enter correct details')
    else:
        return render(request, 'login_user.html', {

    })

def logout_user(request):
    logout(request)
    return redirect('login_user')

def reg_user(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomForm()
    return render(request, 'reg_user.html', {
                'form': form
            })

