#-*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from blog.models import Article
from blog.forms import contactForm


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


def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = contactForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = contactForm()  # Nous créons un formulaire vide

    return render(request, 'blog/contact.html', locals())