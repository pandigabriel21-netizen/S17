import unittest
from livre_s17 import Livre
import catalogue

class TestCatalogue(unittest.TestCase):

    def setUp(self):
        self.livre_1984 = Livre("1984", "Orwell", "9780451524935", 328, 1949)
        self.livre_ferme = Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945)
        self.livre_monde = Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932)
        self.livre_f451 = Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953)
        
        self.catalogue_base = [
            self.livre_1984, 
            self.livre_ferme, 
            self.livre_monde, 
            self.livre_f451
        ]
        
        self.doublon = Livre("1984 (réédition)", "Orwell", "9780451524935", 328, 1949)

    def test_trier_par_titre(self):
        resultat = catalogue.trier_par_titre(self.catalogue_base)
        titres = [l.titre for l in resultat]
        attendu = ['1984', 'Fahrenheit 451', 'La Ferme des animaux', 'Le Meilleur des mondes']
        self.assertEqual(titres, attendu)

    def test_non_modification_du_catalogue(self):
        catalogue_original = list(self.catalogue_base)
        catalogue.trier_par_titre(self.catalogue_base)
        self.assertEqual(self.catalogue_base, catalogue_original)

    def test_trier_par_auteur_puis_annee_recente(self):
        resultat = catalogue.trier_par_auteur_puis_annee_recente(self.catalogue_base)
        auteurs_annees = [(l.auteur, l.annee) for l in resultat]
        attendu = [('Bradbury', 1953), ('Huxley', 1932), ('Orwell', 1949), ('Orwell', 1945)]
        self.assertEqual(auteurs_annees, attendu)

    def test_rechercher_par_isbn(self):
        livre_trouve = catalogue.rechercher_par_isbn(self.catalogue_base, "9780451524935")
        self.assertIsNotNone(livre_trouve)
        self.assertEqual(livre_trouve.titre, "1984") 
        
        livre_absent = catalogue.rechercher_par_isbn(self.catalogue_base, "0000000000000")
        self.assertIsNone(livre_absent)

    def test_dedoublonnage(self):
        avec_doublon = self.catalogue_base + [self.doublon]
        self.assertEqual(catalogue.compter_distincts(avec_doublon), 4)
        
        sans_doublon = catalogue.dedoublonner(avec_doublon)
        self.assertEqual(len(sans_doublon), 4)
        self.assertEqual(sans_doublon[0].titre, "1984")

    def test_regrouper_par_auteur(self):
        groupes = catalogue.regrouper_par_auteur(self.catalogue_base)
        self.assertIn("Orwell", groupes)
        self.assertEqual(len(groupes["Orwell"]), 2)
        
        titres_orwell = [l.titre for l in groupes["Orwell"]]
        self.assertEqual(titres_orwell, ['1984', 'La Ferme des animaux'])

if __name__ == '__main__':
    unittest.main()