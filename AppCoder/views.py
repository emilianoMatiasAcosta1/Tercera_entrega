from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
        return HttpResponse("Hola, esta es mi primera aplicacion")

def saludar_a(request,nombre,apellido=""):
        return HttpResponse(f"hola como estas {nombre.capitalize()} {apellido.capitalize()}")


