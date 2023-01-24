from re import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Template, Context, loader
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import CustomCreationForm

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