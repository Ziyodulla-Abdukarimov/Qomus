from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth import authenticate, login as authlogin, logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        login = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            CustomUser.objects.create_user(username=login, password=password1, user_type=3).save()
    return render(request, 'accounts/register.html')


def login(request):
    login = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=login, password=password)
    authlogin(request, user)

    return render(request, 'accounts/login.html')
