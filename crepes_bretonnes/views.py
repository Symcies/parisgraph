from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


def accueil(request):    
    lieux = {
        0 : ['Jardin du Luxembourg' , 48.8462252, 2.3349718],
        1 : ['Hôpital du val de Grâce' , 48.8488413, 2.3498461],
        2 : ['Statue Equestre d\'Henri IV' , 48.8574652, 2.3404172],
        3 : ['Musée d\'Orsay' , 48.8599649, 2.3243727],      
    }
    return render(request, 'nogit.html', {'lieux':lieux})