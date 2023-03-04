from re import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Template, Context, loader
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .forms import CustomCreationForm
from random import *
import time
import os
from pathlib import Path
from django.contrib import messages

def index(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(str(BASE_DIR) + "asd")

    ctx = {}
    return render(request, 'html/index.html', ctx)

def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login', "redi=dashboard")

    return render(request, 'html/paneles/dashboard.html')

def loginArg(request, rdc):

    obj = loginCall(request, rdc)

    return obj

def loginNoArg(request):

    obj = loginCall(request, None)

    return obj

def loginCall(request, rdc):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if rdc is None:
        rdc = "index"
    else:
        rdc = rdc.replace("redi=", "")

    page = 'login'

    if request.user.is_authenticated:
        return redirect(rdc)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')
            return render(request, 'html/registration/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else rdc)

        else:
            messages.error(request, 'El usuario o contraseña son incorrectos')

    return render(request, 'html/registration/login.html')


def exit(request):
    logout(request)
    return redirect('index')



def regArg(request, usr):

    obj = register(request, usr)

    return obj

def regNoArg(request):

    obj = register(request, None)

    return obj

def register(request, usr):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if usr is None:
        ctx = {
            'form' : CustomCreationForm(),
            'haserrors' : False,
            'usr' : ''
        }
    else:
        ctx = {
            'form' : CustomCreationForm(),
            'haserrors' : False,
            'usr' : usr
        }

    if request.method == 'POST':
        user_creation_form = CustomCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(request, username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            
            login(request, user)
            return redirect('index')
        else:
            ctx['haserrors'] = True

    return render(request, 'html/registration/register.html', ctx)


def actividad_T(request):

    return render(request, 'html/actividad_prueba2/actividad_T.html')



#views de carpeta actividad_prueba2
def actividad_prueba(request):

    var1_1 = randrange(1, 20)
    var1_2 = randrange(1, 20)

    var2_1 = randrange(1, 20)
    var2_2 = randrange(1, 20)

    var3_1 = randrange(1, 20)
    var3_2 = randrange(1, 20)

    var4_1 = randrange(1, 20)
    var4_2 = randrange(1, 20)

    var5_1 = randrange(1, 20)
    var5_2 = randrange(1, 20)

    ctx = {
        "var1_1":var1_1, "var1_2":var1_2,
        "var2_1":var2_1, "var2_2":var2_2,
        "var3_1":var3_1, "var3_2":var3_2,
        "var4_1":var4_1, "var4_2":var4_2,
        "var5_1":var5_1, "var5_2":var5_2,

        "r1":var1_1 + var1_2, "r2":var2_1 + var2_2,
        "r3":var3_1 + var3_2, "r4":var4_1 + var4_2,
        "r5":var5_1 + var5_2,
    }

    return render(request, "html/actividad_prueba2/actividad_prueba.html", ctx)

def resultado(request,r1,r2,r3,r4,r5):

    res1 = request.GET["res1"]
    res2 = request.GET["res2"]
    res3 = request.GET["res3"]
    res4 = request.GET["res4"]
    res5 = request.GET["res5"]

    res = 0
    s = "false"
    bol = "false"

    if res1 == "" or res2 == "" or res3 == "" or res4 == "" or res5 == "":
        s = "true"
    
    if res1 == str(r1):
        res += 1
    if res2 == str(r2):
        res += 1
    if res3 == str(r3):
        res += 1
    if res4 == str(r4):
        res += 1
    if res5 == str(r5):
        res += 1

    if res <= 2:
        bol = "true"

    return render(request, "html/actividad_prueba2/resultado.html", {"res":res, "s":s, "bol":bol})