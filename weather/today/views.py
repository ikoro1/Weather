import requests
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import WeatherCollection
import logging

logger = logging.getLogger(__name__)


class HistoryWeatherView(generic.ListView):
    model = WeatherCollection

class DeleteWeatherView(generic.DeleteView):
    model = WeatherCollection
    success_url = reverse_lazy('weather')



def weather(request):
    api_key = '5f967d8e7a32f28255ccffca6fcf6ef0'
    city_weather = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric'.format(
                city, api_key)
        response = requests.get(url).json()
        if response['cod'] == 200:
            city_weather = {
                'city': response['name'],
                'country': response['sys']['country'],
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon']
            }
            WeatherCollection.objects.create(city=city,
                                             country=city_weather[
                                                 'country'],
                                             temperature=city_weather[
                                                 'temperature'],
                                             weather_description=city_weather[
                                                 'description'] )
        else:
            city_weather = {'error': 'City not found'}
    elif request.method == 'GET':
        city_weather = {}

    return render(request, 'today/weather.html',
                  {'city_weather': city_weather})
