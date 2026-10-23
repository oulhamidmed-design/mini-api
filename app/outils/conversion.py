"""Fonctions de conversion de l'API."""

from math import isfinite

ZERO_ABSOLU_C = -273.15
MILES_PAR_KM = 0.621371
# Taux fixes et indicatifs : 1 euro = X unités de la devise.
TAUX_EURO = {"USD": 1.08, "GBP": 0.85, "JPY": 160.0, "CHF": 0.95}


def celsius_fahrenheit(celsius: float) -> float:
    """Convertit des degrés Celsius en Fahrenheit (arrondi à 2 décimales).

    Lève ValueError si la valeur n'est pas finie ou est sous le zéro absolu.
    """
    if not isfinite(celsius):
        raise ValueError("la température doit être un nombre fini")
    if celsius < ZERO_ABSOLU_C:
        raise ValueError("la température est inférieure au zéro absolu (-273.15)")
    return round(celsius * 9 / 5 + 32, 2)


def km_miles(km: float) -> float:
    """Convertit des kilomètres en miles (arrondi à 4 décimales)."""
    if not isfinite(km) or km < 0:
        raise ValueError("la distance doit être un nombre positif")
    return round(km * MILES_PAR_KM, 4)


def euros_devise(montant: float, devise: str) -> float:
    """Convertit un montant en euros vers une devise (taux fixes indicatifs).

    Lève ValueError si le montant est invalide ou la devise inconnue.
    """
    if not isfinite(montant) or montant < 0:
        raise ValueError("le montant doit être un nombre positif")
    code = devise.upper()
    if code not in TAUX_EURO:
        choix = ", ".join(TAUX_EURO)
        raise ValueError(f"devise inconnue : {devise} (choix possibles : {choix})")
    return round(montant * TAUX_EURO[code], 2)
