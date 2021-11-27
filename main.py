from lib.weather import get_weather
from lib.dictionary import get_definition
from lib.command import Command
import cmd




class Chatbot(cmd.Cmd):

    prompt = '(chatbot) '
    history = []

    def do_meteo(self, line):
        get_weather(line.split())
    
    def do_definition(self, line):
        get_definition(line.split())

    def do_exit(self,line):
        return True

def loop():
    while True:
        e = input('>>>')
        if "/bot" in e:
            Chatbot().cmdloop()



if __name__ == "__main__":
    loop()

