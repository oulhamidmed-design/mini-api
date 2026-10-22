import pytest

from app.outils import math as outils_math


def test_factorielle_cas_normal():
    assert outils_math.factorielle(5) == 120


def test_factorielle_cas_limite():
    assert outils_math.factorielle(0) == 1
    assert outils_math.factorielle(1) == 1


def test_factorielle_erreur():
    with pytest.raises(ValueError):
        outils_math.factorielle(-1)
    with pytest.raises(ValueError):
        outils_math.factorielle(1001)


def test_est_premier_cas_normal():
    assert outils_math.est_premier(7) is True
    assert outils_math.est_premier(10) is False


def test_est_premier_cas_limite():
    assert outils_math.est_premier(0) is False
    assert outils_math.est_premier(1) is False
    assert outils_math.est_premier(2) is True


def test_est_premier_erreur():
    with pytest.raises(ValueError):
        outils_math.est_premier(-3)
    with pytest.raises(ValueError):
        outils_math.est_premier(10**9 + 1)


def test_pgcd_cas_normal():
    assert outils_math.pgcd(12, 18) == 6


def test_pgcd_cas_limite():
    assert outils_math.pgcd(0, 5) == 5
    assert outils_math.pgcd(5, 0) == 5
    assert outils_math.pgcd(7, 7) == 7


def test_pgcd_erreur():
    with pytest.raises(ValueError):
        outils_math.pgcd(-1, 5)
    with pytest.raises(ValueError):
        outils_math.pgcd(0, 0)
