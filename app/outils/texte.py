"""Fonctions de traitement de texte de l'API."""

import unicodedata

LONGUEUR_MAX = 1000
VOYELLES = "aeiouy"


def _verifier(texte: str) -> None:
    """Lève ValueError si le texte est vide ou trop long."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("le texte ne doit pas être vide")
    if len(texte) > LONGUEUR_MAX:
        raise ValueError(f"le texte ne doit pas dépasser {LONGUEUR_MAX} caractères")


def _normaliser(texte: str) -> str:
    """Passe en minuscules et retire les accents."""
    decompose = unicodedata.normalize("NFD", texte.lower())
    return "".join(c for c in decompose if not unicodedata.combining(c))


def est_palindrome(texte: str) -> bool:
    """Indique si le texte se lit pareil dans les deux sens.

    La casse, les accents, les espaces et la ponctuation sont ignorés.
    """
    _verifier(texte)
    lettres = [c for c in _normaliser(texte) if c.isalnum()]
    if not lettres:
        raise ValueError("le texte doit contenir au moins une lettre ou un chiffre")
    return lettres == lettres[::-1]


def compter_voyelles(texte: str) -> int:
    """Compte les voyelles (a, e, i, o, u, y), accents et casse ignorés."""
    _verifier(texte)
    return sum(1 for c in _normaliser(texte) if c in VOYELLES)


def inverser(texte: str) -> str:
    """Renvoie le texte à l'envers."""
    _verifier(texte)
    return texte[::-1]
