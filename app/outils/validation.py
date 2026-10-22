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


def mdp_robuste(mdp: str) -> bool:
    """Un mot de passe est robuste s'il a au moins 8 caractères dont une minuscule,
    une majuscule, un chiffre et un caractère spécial."""
    _verifier(mdp)
    return (
        len(mdp) >= 8
        and any(c.islower() for c in mdp)
        and any(c.isupper() for c in mdp)
        and any(c.isdigit() for c in mdp)
        and any(not c.isalnum() for c in mdp)
    )


def code_postal(cp: str) -> bool:
    """Indique si cp est un code postal français plausible.

    Il faut 5 chiffres, avec un département compris entre 01 et 98.
    """
    _verifier(cp)
    return REGEX_CODE_POSTAL.fullmatch(cp) is not None
