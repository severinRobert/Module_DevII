from lib.weather import Weather
from lib.dictionary import Dictionary
import cmd
import datetime


class Shell(cmd.Cmd):

    prompt = '(chatbot) '
    
    def do_meteo(self, args):
        args = args.split()
        location = args[0]
        hour = None if len(args) != 2 or args[1][-1].upper() != 'H' else int(args[1][:-1])
        day = None if len(args) != 2 else args[1]
        weather = Weather(1, location, hour, day)
        weather.get_weather()
        print(weather)

    def do_definition(self, word):
        definitions = Dictionary(1, word)
        print(definitions)

    def do_exit(self, line):
        return True


def loop():
    while True:
        e = input('>>>')
        if "/bot" in e:
            Shell().cmdloop()



if __name__ == "__main__":
    Shell().cmdloop()
    #loop()

