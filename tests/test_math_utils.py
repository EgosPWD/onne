from math_utils import es_par, suma


def test_suma_basica() -> None:
    assert suma(2, 3) == 5


def test_es_par_basico() -> None:
    assert es_par(4) is True
    assert es_par(5) is False
