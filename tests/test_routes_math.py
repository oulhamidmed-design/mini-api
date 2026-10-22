from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_factorielle():
    r = client.get("/factorielle/5")
    assert r.status_code == 200
    assert r.json() == {"n": 5, "resultat": 120}


def test_route_factorielle_negatif():
    assert client.get("/factorielle/-1").status_code == 400


def test_route_factorielle_pas_un_entier():
    assert client.get("/factorielle/abc").status_code == 400
