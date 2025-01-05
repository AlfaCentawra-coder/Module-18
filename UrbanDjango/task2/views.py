from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def class_temp(request):
    return render(request, 'class_template.html')

class func_temp(TemplateView):
    template_name = 'func_template.html'