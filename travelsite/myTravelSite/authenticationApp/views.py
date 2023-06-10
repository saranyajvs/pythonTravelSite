from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register1(request):
    return render(request, 'Register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwrd = request.POST['password']
        usercheck = auth.authenticate(username=uname, password=pwrd)
        if usercheck is not None:
            auth.login(request, usercheck)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Login')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pwrd = request.POST['password']
        cpwrd = request.POST['confpassword']
        if pwrd == cpwrd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username Exists! try different one!")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=pwrd, first_name=fname, last_name=lname,
                                                email=email)
                messages.info(request, 'User Created!')
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

