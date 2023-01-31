from re import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Template, Context, loader
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import CustomCreationForm
from random import *
import time
from pathlib import Path

def index(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(str(BASE_DIR) + "asd")
    file = 'html/index.html'

    ctx = {}
    return render(request, 'html/index.html', ctx)

@login_required
def dashboard(request):
    doc = loader.get_template('html/dashboard.html')
    ctx = {}
    html = doc.render(ctx)

    return HttpResponse(html)

def login(request):
    doc = loader.get_template('html/login.html')
    ctx = {}
    html = doc.render(ctx)

    return HttpResponse(html)

def loginCall(request):
    ispost = False
    if request.method == 'POST':
        ispost = True

def exit(request):
    logout(request)
    return redirect('index')

def register(request):
    ctx = {
        'form' : CustomCreationForm()
    }
    return render(request, 'registration/register.html', ctx)


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
    s = "string cualquiera"

    if res1 == "" or res2 == "" or res3 == "" or res4 == "" or res5 == "":
        s = "No respondiste todas las preguntas, puedes volver a ver estas actividades"
    
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

    print("res =",res)  

    return render(request, "html/actividad_prueba2/resultado.html", {"res":res, "s":s})