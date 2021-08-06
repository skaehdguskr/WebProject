from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['user_name'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('community/login.html')
        return render(request, 'community/account.html')
    return render(request, 'community/account.html')

# 로그인
def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'community/login.html', {'error': 'user_name or password is incorrect.'})
    else:
        return render(request, 'community/login.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('/')


# home
def home(request):
    return render(request, 'community/board.html')