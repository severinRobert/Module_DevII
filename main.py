import python_weather

def loop():
    running=True
    while running:
        command = input("Entrez votre commande : ")
        manage_command(command)

def manage_command(command):
    command = command.split()
    if command[0] == "weather":
        getweather(command[1])


def getweather(location):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(location)

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop()