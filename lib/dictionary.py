from larousse_api import larousse
from lib.command import Command


class Dictionary(Command):

    def get_definition(self, word:list):
        definitions = larousse.get_definitions(" ".join(word))
        for definition in definitions:
            print(definition)
        print("Source : Larousse\n")