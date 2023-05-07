import requests
import os
from datetime import datetime

user_api = ('b3e462a3a610c4e69001fdef33c4a56f')
location = input('Enter the city name: ')

complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print('Invalid City {}, Please check your City Name'.format(location))

else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed'] # fix the KeyError here
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    faren = (temp_city * (9/5)) + 32

    print('---------------------------------------------------------------')
    print('Weather Stats for - {} || {}'.format(location.upper(),date_time))
    print('---------------------------------------------------------------')

    print(f'Current temperature is: {faren:.2f}')
    print(f'Current weather desc  : {weather_desc}')
    print(f'Current humidity      : {hmdt}')
    print(f'Current wind speed    : {wind_spd}')
