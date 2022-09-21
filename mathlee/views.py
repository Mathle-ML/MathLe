from re import template
from django.http import HttpResponse
from django.template import Template, Context, loader

def auth(request, type):
    if type == "iniciarsesion":
        #doc = open("C:/Users/Nestor Emmanuel/DjangoWorkspaces/mathlee/mathlee/access/html/auth/login.html")
        doc = loader.get_template('login.html')
        bol = False

        #plt = Template(doc.read())
        #doc.close()
        ctx = {"bol": bol}

        html = doc.render(ctx)
    elif type == "registrarte":
        html = "Registrarte"
    return HttpResponse(html)
