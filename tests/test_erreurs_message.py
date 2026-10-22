from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.erreurs import installer_gestionnaires


def creer_client():
    app = FastAPI()
    installer_gestionnaires(app)

    @app.get("/double/{n}")
    def double(n: int):
        return {"n": n * 2}

    return TestClient(app)


def test_message_explicite():
    r = creer_client().get("/double/abc")
    assert r.json()["detail"] == "entrée invalide : type de paramètre incorrect"
