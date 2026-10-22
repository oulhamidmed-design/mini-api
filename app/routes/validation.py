from fastapi import APIRouter

from app.erreurs import erreur_400
from app.outils import validation as outils_validation

router = APIRouter()


@router.get("/email/{email}")
def route_email(email: str):
    try:
        return {"email": email, "valide": outils_validation.email_valide(email)}
    except ValueError as e:
        raise erreur_400(str(e)) from e


@router.get("/mot-de-passe/{mdp}")
def route_mdp(mdp: str):
    # Le mot de passe n'est volontairement pas renvoyé dans la réponse.
    try:
        return {"robuste": outils_validation.mdp_robuste(mdp)}
    except ValueError as e:
        raise erreur_400(str(e)) from e


@router.get("/code-postal/{cp}")
def route_code_postal(cp: str):
    try:
        return {"code_postal": cp, "valide": outils_validation.code_postal(cp)}
    except ValueError as e:
        raise erreur_400(str(e)) from e
