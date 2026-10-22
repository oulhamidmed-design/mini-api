"""Gestion des erreurs de l'API (fichier partagé par tous les modules)."""

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def erreur_400(message: str) -> HTTPException:
    """Construit l'erreur HTTP 400 renvoyée quand l'entrée est invalide."""
    return HTTPException(status_code=400, detail=message)


def installer_gestionnaires(app: FastAPI) -> None:
    """Renvoie 400 (et non 422) quand un paramètre de l'URL a un mauvais type."""

    @app.exception_handler(RequestValidationError)
    async def entree_invalide(request: Request, exc: RequestValidationError):
        return JSONResponse(status_code=400, content={"detail": "entrée invalide"})
