from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_celsius():
    r = client.get("/celsius/100")
    assert r.status_code == 200
    assert r.json() == {"celsius": 100.0, "fahrenheit": 212.0}


def test_route_celsius_sous_le_zero_absolu():
    assert client.get("/celsius/-300").status_code == 400


def test_route_celsius_pas_un_nombre():
    assert client.get("/celsius/abc").status_code == 400


def test_route_km_miles():
    r = client.get("/km-miles/10")
    assert r.status_code == 200
    assert r.json() == {"km": 10.0, "miles": 6.2137}


def test_route_km_miles_negatif():
    assert client.get("/km-miles/-1").status_code == 400


def test_route_euros():
    r = client.get("/euros/100/usd")
    assert r.status_code == 200
    assert r.json() == {"euros": 100.0, "devise": "USD", "resultat": 108.0}


def test_route_euros_devise_inconnue():
    assert client.get("/euros/100/XXX").status_code == 400
