"""Module catalogue - Squelette à compléter (soirée 17).

Ce fichier fournit la STRUCTURE des fonctions à écrire : nom, paramètres
et contrat (ce qui entre, ce qui sort). Il ne contient AUCUN algorithme.

Les spécifications complètes (comportement attendu, cas limites, exemples)
figurent dans l'énoncé de l'atelier TP, qui fait seul autorité. Remplacez
chaque « raise NotImplementedError » par votre implémentation.

Aucune fonction ne doit modifier la liste reçue en argument.

Fichier distribué aux étudiants - à compléter.

Programmation Orientée Objet - EICPN 2025-2026.
"""

from collections import defaultdict  # noqa: F401 (utile selon votre choix)


# ──────────────────────────────────────────────────────────────────────
# 1. Tris
# ──────────────────────────────────────────────────────────────────────

def trier_par_titre(livres):
   return sorted(livres, key=lambda l: l.titre)

def trier_par_auteur_puis_titre(livres):
   return sorted(livres, key=lambda l: (l.auteur, l.titre))

def trier_par_annee(livres, recents_dabord=False):
   return sorted(livres, key=lambda l: l.annee, reverse=recents_dabord)

def trier_par_auteur_puis_annee_recente(livres):
    return sorted(livres, key=lambda l: (l.auteur, -l.annee))

# ──────────────────────────────────────────────────────────────────────
# 2. Recherches
# ──────────────────────────────────────────────────────────────────────

def rechercher_par_auteur(livres, auteur):
    return [l for l in livres if l.auteur == auteur]


def rechercher_par_isbn(livres, isbn):
    for livre in livres:
        if livre.isbn == isbn:
            return livre
    return None
# ──────────────────────────────────────────────────────────────────────
# 3. Ensembles
# ──────────────────────────────────────────────────────────────────────

def compter_distincts(livres):
   return len(set(livres))

def dedoublonner(livres):
   return list(dict.fromkeys(livres))

# ──────────────────────────────────────────────────────────────────────
# 4. Dictionnaires
# ──────────────────────────────────────────────────────────────────────

def indexer_par_isbn(livres):
   return {l.isbn: l for l in livres}

def regrouper_par_auteur(livres):
    groupes = {}
    for livre in livres:
        groupes.setdefault(livre.auteur, []).append(livre)
    return groupes

