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
