from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
'''def homePageView(request):
    return HttpResponse('<h1>"Hello, World!"</h1>')'''

from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'
