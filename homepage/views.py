import json

from django.http import HttpResponse
from django.template import loader

from django.core.cache import cache

# Create your views here.
def homepage(request):
    weather = json.loads(cache.get("weather"))

    template = loader.get_template('homepage.html')

    try:
      temp = round(weather["main"]["temp"] - 272, 2)
      feelslike = round(weather["main"]["feels_like"] - 272, 2)
      humidity = weather["main"]["humidity"]
      city = weather["name"]

    except:
       return HttpResponse(template.render(context, request))

    context = {
        'temp': temp,
        'feelslike': feelslike,
        'humidity': humidity,
        'city': city

    }

    return HttpResponse(template.render(context, request))
