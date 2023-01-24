from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    
    if request.method == "POST":
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User exist already')
                return redirect(register)
            else:
                user= User.objects.create_user(username=username,name=name,email=email,password=password)
                user.set_password(password)
                user.save()
                
                return redirect('login user')

    else:
        print("this is not post methode")
    return render(request,"register.html")



def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
       
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Usernae or Password')
            return redirect('login_user')
    else:
        return render(request,"login.html")


def logout_user(request):
    auth.logout(request)
    return redirect('home')