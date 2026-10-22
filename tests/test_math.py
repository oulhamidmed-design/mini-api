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
