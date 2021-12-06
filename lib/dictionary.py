from larousse_api import larousse


class Dictionary:

    def get_definition(self, word:list):
        definitions = larousse.get_definitions(" ".join(word))
        for definition in definitions:
            print(definition)
        print("Source : Larousse\n")