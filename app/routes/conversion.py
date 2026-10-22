from fastapi import APIRouter

from app.erreurs import erreur_400
from app.outils import conversion as outils_conversion

router = APIRouter()


@router.get("/celsius/{valeur}")
def route_celsius(valeur: float):
    try:
        resultat = outils_conversion.celsius_fahrenheit(valeur)
        return {"celsius": valeur, "fahrenheit": resultat}
    except ValueError as e:
        raise erreur_400(str(e)) from e


@router.get("/km-miles/{km}")
def route_km_miles(km: float):
    try:
        return {"km": km, "miles": outils_conversion.km_miles(km)}
    except ValueError as e:
        raise erreur_400(str(e)) from e


@router.get("/euros/{montant}/{devise}")
def route_euros(montant: float, devise: str):
    try:
        resultat = outils_conversion.euros_devise(montant, devise)
        return {"euros": montant, "devise": devise.upper(), "resultat": resultat}
    except ValueError as e:
        raise erreur_400(str(e)) from e
