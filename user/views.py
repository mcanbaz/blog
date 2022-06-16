from django.shortcuts import render,redirect
from django.contrib import messages
# from . import forms # from . forms
from .forms import RegisterForm,LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid(): # clean metodu cagriliyor
        try:
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)
            messages.success(request,"Başarıyla kayıt oldunuz.")
            return redirect("index")
        except:
            messages.error(request,"Hata oluştu")
            return redirect("index")


    context={"form":form}
    return render(request,"register.html",context) 
    
    """
    # 1 .secenek
    form = RegisterForm()
    context={"form":form}
    return render(request,"register.html",context) 

    # 2.secenek
    if request.method=="POST":
        form = RegisterForm(request.POST)

        if form.is_valid(): # clean metodu cagriliyor
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)
            return redirect("index")


        context={"form":form}
        return render(request,"register.html",context) 
    else:
        form = RegisterForm()
        context={"form":form}
        return render(request,"register.html",context) """

def loginuser(request):
    form = LoginForm(request.POST or None)
    context={"form":form}

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        # clean methodu tanımlanmadiginda mevcut clean fonksiyonu calisiyor, miras alip degistirmistik.
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Kullanıcı adı veya Parola hatalı!")
            return render(request,"login.html",context) 

        messages.success(request,"Giriş başarılı!")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context) 

def logoutuser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız!")
    return redirect("index")