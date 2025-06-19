"""
Calculadora súper simple para aprender pytest.
"""


def sumar(a, b):
    """Suma dos números."""
    return a + b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b 

def restar(a, b):
    """Resta dos números."""
    return a - b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(a, b):
    """Eleva un número a la potencia de otro."""
    return a ** b