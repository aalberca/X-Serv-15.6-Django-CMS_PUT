from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def pagina(request, identificador):

    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
    except Pages.DoesNotExist:
        respuesta = "No existe ese nombre con contenidos en la base de datos"
    return HttpResponse(respuesta)

def muestra_todo(request):
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)

@csrf_exempt
def nueva_pagina(request, nombre, contenido):
    if request.method == "GET":
        nueva_pag = Pages(name = nombre, page = contenido)
        nueva_pag.save()
    elif request.method == "PUT" or request.method == "POST":
        nueva_pag = Pages(name = nombre, page = request.body)
        nueva_pag.save()
    return HttpResponse("Pagina anadida correctamente")
