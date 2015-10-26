from django.shortcuts import render


# Create your views here.


def function0(request):
    snippets = 'Part of the code'
    return render(request, 'snippets/awesome.html', locals())