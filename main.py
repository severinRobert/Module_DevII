
from lib.weather import get_weather
from lib.dictionary import get_definition
from lib.command import Command

def manage_command(command:Command):
        if command.name.lower() == "meteo":
            get_weather(command.arguments)
        elif command.name.lower() == "definition":
            get_definition(command.arguments)
        elif command.name.lower() == "hello":
            print("Hello !")
        elif command.name == "exit":
            exit()


def loop():
    while True:
        command = input("Entrez votre commande : ")
        command = Command(command.split())
        manage_command(command)


if __name__ == "__main__":
    loop()