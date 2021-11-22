import requests
import datetime

def get_weather(arguments: list):
    WEATHER_APIKEY = "ba71f5ff6d30856ebd20ab63054e9e1b"
    LANG = "fr"
    location = arguments[0]
    request = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_APIKEY}&lang={LANG}&units=metric'

    try:
        data = requests.get(request).json()
        if str(data["cod"]) == '404':
            print("La ville indiquée n'a pas été trouvée.")
        elif str(data["cod"]) == '200':
            if len(arguments) > 1:
                latitude = data['coord']['lat']
                longitude = data['coord']['lon']

                data = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=current,minutely&appid={WEATHER_APIKEY}&lang={LANG}&units=metric').json()
                for i in data['hourly']:
                    print(i['dt'])
                    time = (datetime.datetime.now).total_seconds()
                    #if i['dt'] == time - time%3600:
                    #    pass
                print(data['hourly'])
                print(f'Location : {location}')
                print(f'Location : {location}')
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