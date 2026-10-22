import pytest

from app.outils import texte as outils_texte


def test_est_palindrome_cas_normal():
    assert outils_texte.est_palindrome("Radar") is True
    assert outils_texte.est_palindrome("Python") is False


def test_est_palindrome_cas_limite():
    assert outils_texte.est_palindrome("a") is True
    assert outils_texte.est_palindrome("Esope reste ici et se repose") is True
    assert outils_texte.est_palindrome("Été") is True


def test_est_palindrome_erreur():
    with pytest.raises(ValueError):
        outils_texte.est_palindrome("")
    with pytest.raises(ValueError):
        outils_texte.est_palindrome("!!!")
    with pytest.raises(ValueError):
        outils_texte.est_palindrome("a" * 1001)
