from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf


def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')

def registry(request):
    args={}
    if request.POST:
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = User.objects.create_user(username, email, password)
        user.is_staff=True
        user.save()
        return redirect('/')
    else:
        return render(request, 'registry.html',args)

# Create your views here.
