#-*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def home(request):
    text = """<h1> Premiere vue sous Django</h1>
              <p> Les crepes, c'est bon, surtout en Bretagne </p>"""
    return HttpResponse(text)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
    #render admet (request, chemin vers le template [où blog est un dosser à l'interieur des templates de l'app blog], un dictionnaire de variable)
   
    
def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    return render(request, 'blog/addition.html', locals()) 
    #locals est aussi un dictionnaire qui retourne toutes les variables définies dans la fonction 
    #En l'occurence, locals = {"total": 8, "nombre1": 5, "nombre2": 3, "request": <WSGIRequest ...>}  
    