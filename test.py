import unittest
from lib.dictionary import Dictionary
from lib.weather import Weather
import re

class DictionaryTestCase(unittest.TestCase): 
    def test_mot_existant(self): 
        """Vérification que si on demande une définition d'un mot existant, on obtient une liste de définitions"""
        self.assertTrue(Dictionary(1, "test").definitions[0] != "Le mot 'test' n'a pas été trouvé, mots similaires :")
        
    def test_mot_inexistant(self): 
        """Vérification que si on demande une définition d'un mot inexistant, on obtient une liste de mots similaires"""
        self.assertEqual(Dictionary(1, "jukai").definitions[0],"Le mot 'jukai' n'a pas été trouvé, mots similaires :")
    
    def test_mot_vide(self): 
        """Vérification que si on demande une définition d'un mot vide, on obtient un message d'erreur"""
        self.assertEqual(Dictionary(1, "").definitions[0],"Veuillez indiquer le mot à définir : \"definition <mot>\"")
        
class WeatherTestCase(unittest.TestCase):
    def test_ville_vide(self):
        """Vérification que si on demande la météo sans indiquer une ville, on obtient une erreur qui demande une ville"""
        self.assertEqual(Weather(1).error, "Veuillez indiquer une ville.")
        self.assertEqual(Weather(1, None).error, "Veuillez indiquer une ville.")
        self.assertEqual(Weather(1, "").error, "Veuillez indiquer une ville.")
        
    def test_ville_inexistante(self):
        """Vérification que si on demande la météo d'une ville inexistante, on obtient une erreur qui indique que la ville n'existe pas"""
        self.assertEqual(Weather(1, "jukai").error,"La ville indiquée n'a pas été trouvée.")
    
    def test_ville_existante(self):
        """Vérification que si on demande la météo d'une ville, on obtient sa meteo actuelle"""
        self.assertTrue(re.search("Météo à Bruxelles, BE - aujourd'hui", Weather(1, "Bruxelles").__str__()) is not None)
        self.assertTrue(re.search("Météo à Ottignies, BE - aujourd'hui", Weather(1, "Ottignies").__str__()) is not None)
        self.assertTrue(re.search("Météo à Washington, US - aujourd'hui", Weather(1, "Washington").__str__()) is not None)

    def test_heure_non_valide(self):
        """Vérification que si on demande la météo d'une ville avec une heure non valide, on obtient une erreur"""
        self.assertEqual(Weather(1, "Bruxelles", "24h").error, "Veuillez indiquer une heure valide ('24h' n'est pas valide).")
        self.assertEqual(Weather(1, "Bruxelles", "145h").error, "Veuillez indiquer une heure valide ('145h' n'est pas valide).")

    def test_heure_valide(self):
        """Vérification que si on demande la météo d'une ville avec une heure valide, on obtient sa meteo à cette heure"""
        self.assertTrue(re.search("Météo à Bruxelles, BE - ", Weather(1, "Bruxelles", "23h").__str__()) is not None)
        self.assertTrue(re.search("Météo à Bruxelles, BE - aujourd'hui", Weather(1, "Bruxelles", " ").__str__()) is not None)
        self.assertTrue(re.search("Météo à Bruxelles, BE - ", Weather(1, "Bruxelles", "7H").__str__()) is not None)

if __name__ == '__main__':
    unittest.main()