import requests
import datetime
import time
import math

WEATHER_APIKEY = "ba71f5ff6d30856ebd20ab63054e9e1b"
LANG = "fr"

def get_weather_hourly(hour_asked: int, lat: str, lon: str):
    """Cherche les données météo à l'heure demandée

    Args:
        hour_asked (int): heure de la météo à chercher
        lat (str): latitude du lieu
        lon (str): longitude du lieu

    Returns:
        json: donnée météo
    """
    exclude = 'current,minutely,daily'
    data = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric').json()
    
    # temps actuel en secondes
    current_time = int(time.time()) 
    # avoir l'heure actuelles
    current_hour = datetime.datetime.fromtimestamp(current_time).hour
    # supprimer les min et sec + ajouter les heures pour arriver à l'heure demandée
    hours_to_add = hour_asked - current_hour if hour_asked > current_hour else 24 - current_hour + hour_asked
    weather_time = current_time - current_time%3600 + hours_to_add*3600 
    # Chercher l'heure demandée
    for i in data['hourly']:
        if int(i['dt']) == weather_time:
            return i
    print("Erreur")


def get_weather(arguments: list):
    """Gère l'accès aux données météo

    Args:
        arguments (list): arguments donné par l'utilisateur (lieu, heure/jour)
    """
    location = arguments[0]
    request = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric'

    try:
        data = requests.get(request).json()
        if str(data["cod"]) == '404':
            print("La ville indiquée n'a pas été trouvée.")
        elif str(data["cod"]) == '200':
            # si l'utilisateur indique une heure/jour
            if len(arguments) > 1:
                latitude = data['coord']['lat']
                longitude = data['coord']['lon']
                
                if arguments[1][-1].upper() == "H":
                    hour = get_weather_hourly(int(arguments[1][:-1]), latitude, longitude)
                    print(datetime.datetime.fromtimestamp(hour['dt']))
                    print(hour)
                
                

            # si rien est indiqué après la ville on prend la météo actuelle
            else:
                print(f'Localisation : {location}')
                print(f'Météo : {data["weather"][0]["description"]}')
                print(f'Température : {data["main"]["temp"]}°C')
                print(f'Humidité : {data["main"]["humidity"]}%')

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)