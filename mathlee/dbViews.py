from django.shortcuts import redirect, render
from random import *
from mathlee.levelData import data
from mathlee.views import *

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login', "redi=dashboard")

    niveles = {}
    nc = 0
    for i in data:
        nc += 1
        id = data[i]['text']
        niveles.update({id:{}})
        niveles[id].update({'text':id})

        niveles[id].update({'bott' : []})
        temas = niveles[id]['bott']

        for o in range(1,5):
            temas.append(data[i]['temas']['tema_' + str(o)]['text'])

    dsh_height = 37.5 * nc
    cont_height = 100/nc
    rd = 'nivel_'

    ctx = {
        'list' : niveles,
        'dsh_height' : int(dsh_height),
        'cont_height' : int(cont_height),
        'rd' : rd
    }

    return render(request, 'html/paneles/dashboard.html', ctx)
    #return error404(request)

def temas(request, lvl):

    if not request.user.is_authenticated:
        return redirect('login', "redi=dashboard")
    
    temas = {}
    nc = 0

    try:
        for i in data[lvl]['temas']:
            nc += 1
            id = data[lvl]['temas'][i]['text']
            temas.update({id:{}})
            temas[id].update({'text':id})

            temas[id].update({'bott' : []})
            acts = temas[id]['bott']

            for o in range(1,5):
                acts.append(data[lvl]['temas'][i]['actividades']['act_' + str(o)]['text'])
    except:
        return error404(request)
    
    dsh_height = 37.5 * nc
    cont_height = 100/nc

    rd = lvl + '/tema_'

    ctx = {
        'list' : temas,
        'dsh_height' : int(dsh_height),
        'cont_height' : int(cont_height),
        'nivel' : lvl,
        'rd' : rd
    }

    return render(request, 'html/paneles/dashboard.html', ctx)

def actividades(request, lvl, tma):

    if not request.user.is_authenticated:
        return redirect('login', "redi=dashboard")
    
    actividades = []
    nc = 0
    try:
        for i in data[lvl]['temas'][tma]['actividades']:
            nc += 1
            actividades.append(data[lvl]['temas'][tma]['actividades'][i]['text'])
    except:
        return error404(request)
    
    dsh_height = 20 * nc
    cont_height = 100/nc

    rd = lvl + '/' + tma + '/act_'

    ctx = {
        'list' : actividades,
        'dsh_height' : int(dsh_height),
        'cont_height' : int(cont_height),
        'nivel' : lvl,
        'tema' : tma,
        'rd' : rd
    }


    return render(request, 'html/paneles/dashboard_act.html', ctx)