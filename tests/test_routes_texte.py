from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_palindrome():
    r = client.get("/palindrome/Radar")
    assert r.status_code == 200
    assert r.json() == {"texte": "Radar", "palindrome": True}


def test_route_palindrome_texte_vide():
    assert client.get("/palindrome/%20").status_code == 400


def test_route_voyelles():
    r = client.get("/voyelles/Bonjour")
    assert r.status_code == 200
    assert r.json() == {"texte": "Bonjour", "voyelles": 3}


def test_route_voyelles_texte_vide():
    assert client.get("/voyelles/%20").status_code == 400
