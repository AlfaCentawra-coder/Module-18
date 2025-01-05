from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class pf(TemplateView):
    template_name = 'platform.html'


class ct(TemplateView):
    template_name = 'cart.html'

def gms(request):
    mydict = {'games': ["Like a Dragon: Pirate Yakuza in Hawaii", "Atomfall"]}
    context={
         'mydict':mydict,
    }
    return render(request, 'games.html', context)

