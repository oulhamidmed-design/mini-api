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
