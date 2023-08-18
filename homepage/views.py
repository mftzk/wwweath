from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.core.cache import cache

# Create your views here.
def homepage(request):
    weather = cache.get("weather")
    context = {
        'weather': weather
    }
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context, request))
