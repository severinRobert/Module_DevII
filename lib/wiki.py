import wikipedia


class Wiki:

    def get_resume(self, word: list):

        select_lang = "fr"
        lang = wikipedia.set_lang(select_lang)
        searchs = wikipedia.search(" ".join(word))
        for search in searchs:
            print(search)

        summary = wikipedia.summary(" ".join(word))

        pass


'''wikipedia.set_lang("fr")
j = wikipedia.search("Barack")
h = wikipedia.summary("belgium", sentences=1)

print(h)
'''