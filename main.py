from lib.weather import Weather
from lib.dictionary import get_definition
import cmd




class Chatbot(cmd.Cmd):

    prompt = '(chatbot) '
    history = []

    def do_meteo(self, line):
        weather = Weather()
    
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
    Chatbot().cmdloop()
    #loop()

