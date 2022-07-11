from lib.weather import Weather
from lib.dictionary import Dictionary
import cmd
import datetime


class Shell(cmd.Cmd):

    prompt = '(chatbot) '
    
    def do_meteo(self, args):
        'Recherche la météo d\'une ville : "meteo <ville> [<heure/jour>]"'
        args = args.split()
        location = None if len(args) < 1 else args[0]
        when = None if len(args) < 2 else args[1]
        weather = Weather(1, location, when)
        weather.get_weather()
        print(weather)

    def do_definition(self, word):
        'Recherche la définition d\'un mot : "definition <mot>"'
        definitions = Dictionary(1, word)
        print(definitions)

    def do_exit(self, line):
        'Quitte le programme'
        return True


def loop():
    while True:
        e = input('>>>')
        if "/bot" in e:
            Shell().cmdloop()



if __name__ == "__main__":
    Shell().cmdloop()
    #loop()

