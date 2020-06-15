from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from.forms import UserForm


# Create your views here.
def registerPage(request):
    print(request.POST)
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)

            return redirect('authentication:login')

    context = {'form': form}
    return render(request, 'authentication/registration.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('forum:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'authentication/login.html', context)

def logoutUser(request):
    logout(request)

    return redirect('forum:home')