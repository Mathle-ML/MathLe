from django.shortcuts import render
import datetime

# Create your views here.

def pagina_registro(request):

    fecha = datetime.datetime.now()
    color = "amarillo"
    ctx = {"fecha":fecha, "color":color}

    return render(request, "registro.html", ctx)