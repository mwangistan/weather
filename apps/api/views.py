import requests
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from apps.api.utils import Parser
from rest_framework import status
from apps.api.errors import TranslateError
from apps.api.serializer import WeatherSerializer

class TemperatureAPIView(APIView):
    '''Return the minimum, maximum, average and median temperature in celcius
       :param city: City name
       :param days: Number of days of forecast
    '''
    def get(self, request, city, format=None):
        days = request.GET.get('days', None)
        serializer = WeatherSerializer(data={'days':days, 'city':city})

        if serializer.is_valid():
            url = settings.WEATHER_API_URL_V1 + '?key=' + settings.WEATHER_API_KEY + '&q=' + city + '&days=' + days 
            response = requests.get(url)
            data = json.loads(response.content)

            if response.ok:
                max_val = Parser.get_maximum(data['forecast']['forecastday'])
                min_val = Parser.get_minimum(data['forecast']['forecastday'])
                avg_val = Parser.get_average(data['forecast']['forecastday'])
                med_val = Parser.get_median(data['forecast']['forecastday'])

                return Response({'maximum': max_val, 'minimum': min_val, 'average': avg_val, 'median': med_val}, status=status.HTTP_200_OK)
            else:
                err_code = data['error']['code']
                content, status_code =  TranslateError().handle(err_code)
                return Response(content, status=status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)