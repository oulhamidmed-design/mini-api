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
