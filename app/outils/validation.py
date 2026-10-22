"""Fonctions de validation de l'API."""

import re

LONGUEUR_MAX = 254
REGEX_EMAIL = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
)
REGEX_CODE_POSTAL = re.compile(r"(0[1-9]|[1-8][0-9]|9[0-8])[0-9]{3}")


def _verifier(valeur: str) -> None:
    """Lève ValueError si la valeur est vide ou trop longue."""
    if not isinstance(valeur, str) or not valeur.strip():
        raise ValueError("la valeur ne doit pas être vide")
    if len(valeur) > LONGUEUR_MAX:
        raise ValueError(f"la valeur ne doit pas dépasser {LONGUEUR_MAX} caractères")


def email_valide(email: str) -> bool:
    """Indique si l'adresse a une forme d'email valide (nom@domaine.extension)."""
    _verifier(email)
    return REGEX_EMAIL.fullmatch(email) is not None
