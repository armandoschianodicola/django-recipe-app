from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from . import forms


# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, '{} has been created'.format(username))
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('recipes-home')

    form = forms.UserRegistrationForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
