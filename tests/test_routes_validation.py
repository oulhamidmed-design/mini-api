from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_email():
    r = client.get("/email/lea@mail.fr")
    assert r.status_code == 200
    assert r.json() == {"email": "lea@mail.fr", "valide": True}


def test_route_email_invalide():
    r = client.get("/email/pas-un-email")
    assert r.status_code == 200
    assert r.json()["valide"] is False


def test_route_email_vide():
    assert client.get("/email/%20").status_code == 400


def test_route_mdp():
    r = client.get("/mot-de-passe/Motdepasse1!")
    assert r.status_code == 200
    assert r.json() == {"robuste": True}


def test_route_mdp_faible():
    assert client.get("/mot-de-passe/abc").json() == {"robuste": False}


def test_route_mdp_vide():
    assert client.get("/mot-de-passe/%20").status_code == 400
