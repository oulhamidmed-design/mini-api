from fastapi import APIRouter

from app.erreurs import erreur_400
from app.outils import math as outils_math

router = APIRouter()


@router.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": outils_math.factorielle(n)}
    except ValueError as e:
        raise erreur_400(str(e)) from e
