from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.erreurs import erreur_400, installer_gestionnaires


def test_erreur_400_a_le_bon_code():
    assert erreur_400("n négatif").status_code == 400


def test_erreur_400_garde_le_message():
    assert erreur_400("n négatif").detail == "n négatif"


def test_type_invalide_renvoie_400():
    app = FastAPI()
    installer_gestionnaires(app)

    @app.get("/double/{n}")
    def double(n: int):
        return {"n": n * 2}

    client = TestClient(app)
    assert client.get("/double/4").status_code == 200
    assert client.get("/double/abc").status_code == 400
