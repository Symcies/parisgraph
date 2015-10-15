#-*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from blog.models import Article


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
    #render admet (request, chemin vers le template [où blog est un dosser à l'interieur des templates de l'app blog], un dictionnaire de variable)
   
    
def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    return render(request, 'blog/addition.html', locals()) 
    #locals est aussi un dictionnaire qui retourne toutes les variables définies dans la fonction 
    #En l'occurence, locals = {"total": 8, "nombre1": 5, "nombre2": 3, "request": <WSGIRequest ...>}  
    
def accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles':articles})
    
def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/lire.html',{'article' : article})

