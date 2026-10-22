"""Fonctions mathématiques de l'API."""

LIMITE_FACTORIELLE = 1000


def factorielle(n: int) -> int:
    """Renvoie n!. Lève ValueError si n est négatif ou supérieur à 1000."""
    if n < 0:
        raise ValueError("n doit être positif")
    if n > LIMITE_FACTORIELLE:
        raise ValueError(f"n doit être inférieur ou égal à {LIMITE_FACTORIELLE}")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


LIMITE_PREMIER = 10**9


def est_premier(n: int) -> bool:
    """Indique si n est premier. Lève ValueError si n est négatif ou trop grand."""
    if n < 0:
        raise ValueError("n doit être positif")
    if n > LIMITE_PREMIER:
        raise ValueError(f"n doit être inférieur ou égal à {LIMITE_PREMIER}")
    if n < 2:
        return False
    diviseur = 2
    while diviseur * diviseur <= n:
        if n % diviseur == 0:
            return False
        diviseur += 1
    return True


def pgcd(a: int, b: int) -> int:
    """Plus grand commun diviseur de a et b.

    Lève ValueError si a ou b est négatif, ou si les deux valent 0.
    """
    if a < 0 or b < 0:
        raise ValueError("a et b doivent être positifs")
    if a == 0 and b == 0:
        raise ValueError("le pgcd de 0 et 0 n'est pas défini")
    while b:
        a, b = b, a % b
    return a
