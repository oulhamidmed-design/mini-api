from fastapi import APIRouter

from app.erreurs import erreur_400
from app.outils import texte as outils_texte

router = APIRouter()


@router.get("/palindrome/{texte}")
def route_palindrome(texte: str):
    try:
        return {"texte": texte, "palindrome": outils_texte.est_palindrome(texte)}
    except ValueError as e:
        raise erreur_400(str(e)) from e


@router.get("/voyelles/{texte}")
def route_voyelles(texte: str):
    try:
        return {"texte": texte, "voyelles": outils_texte.compter_voyelles(texte)}
    except ValueError as e:
        raise erreur_400(str(e)) from e


@router.get("/inverser/{texte}")
def route_inverser(texte: str):
    try:
        return {"texte": texte, "resultat": outils_texte.inverser(texte)}
    except ValueError as e:
        raise erreur_400(str(e)) from e
