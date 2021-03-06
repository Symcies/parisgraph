"""crepes_bretonnes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from crepes_bretonnes.views import accueil

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^snippets/', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework') ),
    # the rest_framework.urls enables the "login" button to have registered users
    #url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework)) # If using the browsable API -> login and logout views 

    # It is very important that the last URL in the above snippet always be the last URL. 
    #This is known as a passthrough or catch-all route. 
    #It accepts all requests not matched by a previous rule and passes the request through to AngularJS's router for processing. The order of other URLS is normally insignificant.
    url('^.*$', accueil, name='accueil'),
]
