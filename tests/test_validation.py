import pytest

from app.outils import validation as outils_validation


def test_email_valide_cas_normal():
    assert outils_validation.email_valide("lea@mail.fr") is True
    assert outils_validation.email_valide("pas-un-email") is False


def test_email_valide_cas_limite():
    assert outils_validation.email_valide("a@b.co") is True
    assert outils_validation.email_valide("@mail.fr") is False
    assert outils_validation.email_valide("lea@mail") is False


def test_email_valide_erreur():
    with pytest.raises(ValueError):
        outils_validation.email_valide("")
    with pytest.raises(ValueError):
        outils_validation.email_valide("a" * 255)


def test_mdp_robuste_cas_normal():
    assert outils_validation.mdp_robuste("Motdepasse1!") is True
    assert outils_validation.mdp_robuste("motdepasse") is False


def test_mdp_robuste_cas_limite():
    assert outils_validation.mdp_robuste("Abcdef1!") is True
    assert outils_validation.mdp_robuste("Abcde1!") is False
    assert outils_validation.mdp_robuste("abcdefg1!") is False


def test_mdp_robuste_erreur():
    with pytest.raises(ValueError):
        outils_validation.mdp_robuste("")
    with pytest.raises(ValueError):
        outils_validation.mdp_robuste("a" * 255)
