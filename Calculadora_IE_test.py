import pytest
from Calculos import Calculos

def test_comodo():
    local = Calculos('sala', 4, 5)
    assert local.comodo == 'SALA'


def test_calculo_area():
    local = Calculos('sala', 4, 5)
    assert local.calculo_area() == 20.0


def test_calculo_perimetro():
    local = Calculos('sala', 4, 5)
    assert local.calculo_perimetro() == 18.0


def test_potmin_lamp():
    local = Calculos('sala', 4, 5)
    assert local.potmin_lamp() == 280


def test_qntmin_tom():
    local = Calculos('sala', 4, 5)
    assert local.qntmin_tom() == 4
