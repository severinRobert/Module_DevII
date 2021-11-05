import requests


def loop():
    while True:
        command = input("Entrez votre commande : ")
        manage_command(command)


def manage_command(command):
    command = command.split()
    command = clean_command(command)
    if command[0] == "meteo":
        get_weather(command[1])
    elif command[0] == "exit":
        exit()


def clean_command(command):
    new_command = []
    for i in command:
        if i != "":
            new_command.append(i)
    return new_command


def get_weather(location):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APIKEY}&lang={LANG}')
        data = r.json()
        if data["cod"] == 404:
            print("La ville indiquée n'a pas été trouvée.")
        elif data["cod"] == 200:
            print(f'Localisation : {location}')
            print(f'Météo : {data["weather"][0]["description"]}')
            print(f'Température : {round(data["main"]["temp"] - 273.15, 2)}°C')
            print(f'Humidité : {data["main"]["humidity"]}%')

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


if __name__ == "__main__":
    APIKEY = "ba71f5ff6d30856ebd20ab63054e9e1b"
    LANG = "fr"
    loop()
