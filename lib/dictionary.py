from larousse_api import larousse
from lib.command import Command
import requests
import re
import unicodedata
from bs4 import BeautifulSoup


class Dictionary(Command):

    def __init__(self, user: int, word: str) -> None:
        super().__init__(user)
        self.word = word
        self.definitions = self.get_definitions(word)

    def get_definitions(self, word):
        """
        :param word: The word whose definition you are looking for
        :return: A list containing all the definitions of word
        """
        if word == "":
            return ['Veuillez indiquer le mot à définir : "definition <mot>"']

        url = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
        soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')
        for ul in soup.find_all('ul'):
            if ul.get('class') is not None and 'Definitions' in ul.get('class'):
                return [unicodedata.normalize("NFKD", re.sub("<.*?>", "", str(li))) for li in ul.find_all('li')]
        for ul in soup.find_all('ul'):
            if ul.get('class') is None:
                return [f"Le mot '{self.word}' n'a pas été trouvé, mots similaires :"] + [a.string for a in ul.find_all('a')]
        return []

    def __str__(self) -> str:
        str_to_print = ""
        for definition in self.definitions:
            str_to_print += f'{definition}\n'
        str_to_print += "\nSource : Larousse\n"
        return str_to_print