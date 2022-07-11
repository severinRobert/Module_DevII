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
    def test_ville_existante(self):
        """Vérification que si on demande la météo d'une ville existante, on obtient une liste de météo"""
        self.assertTrue()
        
    def test_ville_inexistante(self):
        """Vérification que si on demande la météo d'une ville inexistante, on obtient une liste de météo"""
        self.assertEqual(Weather(1, "jukai").weather[0],"La météo de jukai n'a pas été trouvée")
    
    def test_ville_vide(self):
        """Vérification que si on demande la météo d'une ville vide, on obtient un message d'erreur"""
        self.assertEqual(Weather(1, "").weather[0],"Veuillez indiquer la")

if __name__ == '__main__':
    unittest.main()