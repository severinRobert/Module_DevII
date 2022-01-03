import json
import requests
import datetime
import time
import math
from lib.command import Command

WEATHER_APIKEY = "ba71f5ff6d30856ebd20ab63054e9e1b"
LANG = "fr"


class Weather(Command):
    def __init__(self, user: int, date: datetime, location: str, hour: int = None, day: str = None, weather: json = None) -> None:
        super().__init__(user, date)
        self.__location = location
        self.__hour = hour
        self.__day = day
        self.__weather = weather

    def __str__(self) -> str:
        pass

    def get_weather(self) -> None:
        """Cherche les données météo à l'heure demandée
        """
        request = f'https://api.openweathermap.org/data/2.5/weather?q={self.__location}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric'

        try:
            self.__weather = requests.get(request).json()
            if str(self.__weather["cod"]) == '404':
                print("La ville indiquée n'a pas été trouvée.")
            elif str(self.__weather["cod"]) == '200':
                latitude = self.__weather['coord']['lat']
                longitude = self.__weather['coord']['lon']
                # si l'utilisateur indique une heure/jour
                if self.__hour is not None:
                    self.__weather = self.__get_weather_hourly(latitude, longitude)

                elif self.__day is not None:
                    self.__weather = self.__get_weather_daily(latitude, longitude)

                # si rien est indiqué après la ville on prend la météo actuelle
                else:
                    exclude = 'hourly,minutely,daily'
                    data = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={exclude}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric').json()

                    self.__weather = data["current"]
                print(self)

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)

    def __get_weather_hourly(self, lat: str, lon: str):
        """Cherche les données météo à l'heure demandée

        Args:
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
        hours_to_add = self.__hour - current_hour if self.__hour > current_hour else 24 - current_hour + self.__hour
        weather_time = current_time - current_time % 3600 + hours_to_add*3600
        # Chercher l'heure demandée
        for i in data['hourly']:
            if int(i['dt']) == weather_time:
                return i
        print("Erreur, heure non trouvée")

    def __get_weather_daily(self, lat: str, lon: str):
        """Cherche les données météo à l'heure demandée

        Args:
            lat (str): latitude du lieu
            lon (str): longitude du lieu

        Returns:
            json: donnée météo
        """
        days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
        exclude = 'current,minutely,hourly'
        data = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric').json()

        # temps actuel en secondes
        current_time = int(time.time())
        # avoir l'heure actuelles
        current_day = datetime.datetime.fromtimestamp(current_time).weekday()
        # supprimer les min et sec + ajouter les heures pour arriver à l'heure demandée
        days_to_add = (days.index(self.__day) - current_day) % 7
        self.__weather = data['daily'][days_to_add]

    def __str__(self) -> str:
        days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
        date = datetime.datetime.fromtimestamp(self.__weather["dt"])
        day = days[date.weekday()]
        day = " aujourd'hui" if self.__day is None else f" le {day}"
        hour = "" if self.__hour is None else f" à {self.__hour}h"
        date = " " + date.strftime("%d/%m/%Y")
        temperature = self.__weather["temp"]
        feels_like = self.__weather["feels_like"]
        humidity = self.__weather["humidity"]
        description = self.__weather["weather"][0]["description"]

        str_to_print = f"Météo à {self.__location}{day}{date}{hour}\n"
        str_to_print += f"{description}, {temperature}°C avec un ressenti de {feels_like}°C\n"
        str_to_print += f"{humidity}% d'humidité\n"
        return str_to_print
