from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_palindrome():
    r = client.get("/palindrome/Radar")
    assert r.status_code == 200
    assert r.json() == {"texte": "Radar", "palindrome": True}


def test_route_palindrome_texte_vide():
    assert client.get("/palindrome/%20").status_code == 400
