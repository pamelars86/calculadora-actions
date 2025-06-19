# 🧪 Pytest Súper Simple

![CI](https://github.com/TU_USUARIO/calculadora-actions/workflows/CI%20Pipeline/badge.svg)

Proyecto minimalista para aprender pytest con Poetry.

## 📁 Archivos

- `calculadora.py` - 2 funciones simples
- `test_calculadora.py` - 2 tests básicos
- `pyproject.toml` - Configuración de Poetry

## 🚀 Cómo usar

### 1. Instalar dependencias
```bash
cd pytest_simple
poetry install
```

### 2. Ejecutar tests
```bash
# Ejecutar tests
poetry run pytest

# Con más información
poetry run pytest -v
```

## 🎯 Lo que aprenderás

1. **Función simple**: `sumar(2, 3)` → `5`
2. **Test simple**: `assert sumar(2, 3) == 5`
3. **Ejecutar con Poetry**: `poetry run pytest`

## 🧪 Los 2 tests

```python
def test_sumar():
    resultado = sumar(2, 3)
    assert resultado == 5

def test_multiplicar():
    resultado = multiplicar(4, 5)
    assert resultado == 20
```

¡Solo ejecuta `poetry run pytest -v` y verás la magia! 🎉 