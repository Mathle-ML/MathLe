from re import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Template, Context, loader
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import CustomCreationForm
from random import *
import time

def index(request):
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

    """s = 1
    for s in range(30):
        print(s)
        time.sleep(1)
    """

    return render(request, "actividad_prueba2/actividad_prueba.html", ctx)

def resultado(request,r1,r2,r3,r4,r5):

    res1 = int(request.GET["res1"])
    res2 = int(request.GET["res2"])
    res3 = int(request.GET["res3"])
    res4 = int(request.GET["res4"])
    res5 = int(request.GET["res5"])

    res = 0

    if res1 == r1:
        res += 1
    if res2 == r2:
        res += 1
    if res3 == r3:
        res += 1
    if res4 == r4:
        res += 1
    if res5 == r5:
        res += 1    

    return render(request, "actividad_prueba2/resultado.html", {"res":res})