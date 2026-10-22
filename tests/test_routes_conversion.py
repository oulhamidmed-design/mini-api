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
