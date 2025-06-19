"""
Tests súper simples para aprender pytest.
Solo 2 tests básicos.
"""

from calculadora import sumar, multiplicar, restar, dividir, potencia
import pytest

def test_sumar():
    """Test: verificar que 2 + 3 = 5"""
    resultado = sumar(2, 3)
    assert resultado == 5


def test_multiplicar():
    """Test: verificar que 4 * 5 = 20"""
    resultado = multiplicar(4, 5)
    assert resultado == 20 

def test_restar():
    """Test: verificar que 10 - 5 = 5"""
    resultado = restar(10, 5)
    assert resultado == 5

def test_dividir():
    """Test: verificar que 10 / 2 = 5"""
    resultado = dividir(10, 2)
    assert resultado == 5

def test_dividir_por_cero():
    """Test: verificar que al dividir por cero se lanza una excepción"""
    with pytest.raises(ValueError):
        dividir(10, 0)