from larousse_api import larousse

def get_definition(word:list):
    definitions = larousse.get_definitions(" ".join(word))
    for definition in definitions:
        print(definition)
    print("Source : Larousse\n")