from re import template

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

@login_required
def dashboard(request):
    template_name = 'registration/dashboard.html'
    return render(request, template_name)

def register(request):
    template_name = 'registration/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    return render(request, template_name)

# Create your views here.
