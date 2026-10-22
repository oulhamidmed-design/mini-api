import importlib
import pkgutil

from fastapi import FastAPI

from app import routes
from app.erreurs import installer_gestionnaires

app = FastAPI(title="Mini API")
installer_gestionnaires(app)

# Chaque fichier de app/routes/ expose un `router` : on les branche tous ici.
# Ajouter une route ne demande donc plus de modifier main.py (moins de conflits).
for module in pkgutil.iter_modules(routes.__path__):
    nom = f"{routes.__name__}.{module.name}"
    app.include_router(importlib.import_module(nom).router)


@app.get("/sante")
def sante():
    return {"statut": "ok"}
