import json
import requests
import datetime
import time
from lib.command import Command
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_APIKEY = os.getenv('WEATHER_APIKEY')

LANG = "fr"


class Weather(Command):
    days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

    def __init__(self, user: int, location: str, when: int = None, weather: json = None) -> None:
        super().__init__(user)
        self.__location = location
        self.__hour = when
        self.__day = when
        self.weather = weather
        self.__error = ""

    def __check_params(self):
        """ Vérifie les paramètre donné à la classe """
        if self.__location is None or self.__location == '':
            self.__error = "Veuillez indiquer une ville."
            return 1
        if self.__hour is not None and self.__hour[-1] == 'h' or ( self.__hour[:-1].isdecimal() and int(self.__hour[:-1]) in range(0, 24) ):
            self.__error = f"Veuillez indiquer une heure qui soit valide ('{self.__hour}' n'est pas valide)."
            return 1
        elif self.__day is not None and self.__day not in self.days:
            self.__error = f"Veuillez indiquer un jour valide ('{self.__day}' n'est pas valide)."
            return 1
        return 0

    
    def get_weather(self) -> None:
        """Cherche les données météo à l'heure demandée
        """
        if self.__check_params() == 1:
            return
        request = f'https://api.openweathermap.org/data/2.5/weather?q={self.__location}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric'

        try:
            self.weather = {'cod': '404'} if self.__location=='' or self.__location is None else requests.get(request).json()
            if str(self.weather["cod"]) == '404':
                self.__error = "La ville indiquée n'a pas été trouvée."
            elif str(self.weather["cod"]) == '200':
                latitude = self.weather['coord']['lat']
                longitude = self.weather['coord']['lon']
                self.__location = f"{self.weather['name']}, {self.weather['sys']['country']} "
                # si l'utilisateur indique une heure/jour
                if self.__hour is not None:
                    self.weather = self.__get_weather_hourly(latitude, longitude)

                elif self.__day is not None:
                    self.weather = self.__get_weather_daily(latitude, longitude)

                # si rien est indiqué après la ville on prend la météo actuelle
                else:
                    exclude = 'hourly,minutely,daily'
                    data = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={exclude}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric').json()

                    self.weather = data["current"]

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
        """Cherche les données météo au jour demandé

        Args:
            lat (str): latitude du lieu
            lon (str): longitude du lieu

        Returns:
            json: donnée météo
        """
        exclude = 'current,minutely,hourly'
        data = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric').json()
        # temps actuel en secondes
        current_time = int(time.time())
        # avoir le jour actuel
        current_day = datetime.datetime.fromtimestamp(current_time).weekday()
        # avoir le nombre de jour à ajouter pour arriver au jour demandé
        days_to_add = (self.days.index(self.__day) - current_day) % 7
        self.weather = data['daily'][days_to_add]
        return self.weather

    def __str__(self) -> str:
        if self.__error == "":
            date = datetime.datetime.fromtimestamp(self.weather["dt"])
            day = self.days[date.weekday()]
            day = " aujourd'hui" if self.__day is None else f" le {day}"
            hour = "" if self.__hour is None else f" à {self.__hour}h"
            date = " " + date.strftime("%d/%m/%Y")
            description = self.weather["weather"][0]["description"]
            temperature = f'{self.weather["temp"]}°C' if type(self.weather["temp"]) is float else f"de {self.weather['temp']['min']}°C à {self.weather['temp']['max']}°C"
            feels_like = f'{self.weather["feels_like"]}°C' if type(self.weather["feels_like"]) is float else f"de {self.weather['feels_like']['day']}°C pendant la journée"
            humidity = self.weather["humidity"]

            str_to_print = f"Météo à {self.__location}-{day}{date}{hour}\n"
            str_to_print += f"{description}, {temperature} avec un ressenti de {feels_like}\n"
            str_to_print += f"{humidity}% d'humidité\n"
        else:
            str_to_print = self.__error
        return str_to_print
