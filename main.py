from lib.weather import Weather
from lib.dictionary import Dictionary
import cmd
import datetime


class Shell(cmd.Cmd):

    prompt = '(chatbot) '
    
    def do_meteo(self, line):
        line = line.split()
        location = line[0]
        hour = None if len(line) != 2 or line[1][-1].upper() != 'H' else int(line[1][:-1])
        day = None if len(line) != 2 else line[1]
        weather = Weather(location, hour, day)
        weather.get_weather()

    def do_definition(self, line):
        print(line)
        definitions = Dictionary().get_definition(line.split())

    def do_exit(self, line):
        return True


def loop():
    while True:
        e = input('>>>')
        if "/bot" in e:
            Chatbot().cmdloop()



if __name__ == "__main__":
    Shell().cmdloop()
    #loop()

