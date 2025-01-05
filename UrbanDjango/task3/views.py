from django.shortcuts import render
from django.views.generic import TemplateView

class main1(TemplateView):
    template_name = 'index1.html'

class shop(TemplateView):
    template_name = 'index2.html'

class bascet(TemplateView):
    template_name = 'index3.html'