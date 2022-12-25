from datetime import datetime

import requests
from configs import parameters


def pogodas(city):
    parameters['q'] = city
    try:
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
        temp = data['main']['temp']
        city_name = data['name']
        wind = data['wind']['speed']
        timezone = data['timezone']
        sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise']) + int(timezone)).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.utcfromtimestamp(int(data['sys']['sunset']) + int(timezone)).strftime('%Y-%m-%d %H:%M:%S')
        description = data['weather'][0]['description']
        data_pogoda = {
            'city_name': city_name,
            'temp': temp,
            'wind': wind,
            'timezone': timezone,
            'sunrise': sunrise,
            'sunset': sunset,
            'description': description
        }
        return data_pogoda
    except KeyError:
        return "Вы ввели не корректный город"