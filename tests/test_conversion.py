import pytest

from app.outils import conversion as outils_conversion


def test_celsius_fahrenheit_cas_normal():
    assert outils_conversion.celsius_fahrenheit(100) == 212.0


def test_celsius_fahrenheit_cas_limite():
    assert outils_conversion.celsius_fahrenheit(0) == 32.0
    assert outils_conversion.celsius_fahrenheit(-273.15) == -459.67


def test_celsius_fahrenheit_erreur():
    with pytest.raises(ValueError):
        outils_conversion.celsius_fahrenheit(-300)
    with pytest.raises(ValueError):
        outils_conversion.celsius_fahrenheit(float("inf"))
    with pytest.raises(ValueError):
        outils_conversion.celsius_fahrenheit(float("nan"))


def test_km_miles_cas_normal():
    assert outils_conversion.km_miles(10) == 6.2137


def test_km_miles_cas_limite():
    assert outils_conversion.km_miles(0) == 0.0


def test_km_miles_erreur():
    with pytest.raises(ValueError):
        outils_conversion.km_miles(-1)
    with pytest.raises(ValueError):
        outils_conversion.km_miles(float("nan"))
