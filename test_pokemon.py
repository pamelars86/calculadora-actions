"""
Tests de Pokemon usando unittest.mock con explicaciones detalladas.
"""
import requests
from unittest.mock import Mock, patch
from pokemon import obtener_pokemon


class TestPokemonConUnittestMock:
    """Tests usando unittest.mock - cada decorador explicado."""

    # ===== DECORADOR @patch EXPLICADO =====

    @patch("pokemon.requests.get")  # ← 1. Reemplaza requests.get en el módulo pokemon
    def test_obtener_ditto_explicado(
        self, mock_get
    ):  # ← 2. mock_get es el Mock que reemplazó requests.get
        """
        Test explicado paso a paso:

        @patch hace 3 cosas:
        1. Guarda la función original: requests.get
        2. La reemplaza con un Mock(): pokemon.requests.get = Mock()
        3. Pasa ese Mock como parámetro: mock_get
        """

        # 3. Configuramos el mock - qué debe devolver cuando se llame
        mock_response = Mock()  # ← Creamos un objeto falso para simular response
        mock_response.status_code = 200  # ← response.status_code devuelve 200
        mock_response.json.return_value = {  # ← response.json() devuelve este dict
            "name": "ditto",
            "order": 214,
        }
        mock_get.return_value = mock_response  # ← requests.get() devuelve mock_response

        # 4. Ejecutamos la función que queremos testear
        resultado = obtener_pokemon("ditto")  # ← Internamente llama requests.get()

        # 5. Verificamos el resultado
        assert resultado["success"] is True
        assert resultado["name"] == "ditto"
        assert resultado["order"] == 214

        # 6. Verificamos que se hizo la llamada correcta al mock
        mock_get.assert_called_once_with(
            "https://pokeapi.co/api/v2/pokemon/ditto", timeout=10
        )

        # En este punto @patch automáticamente restaura requests.get original

    # ===== SIMULANDO EXCEPCIONES =====

    @patch("pokemon.requests.get")
    def test_timeout_con_side_effect(self, mock_get):
        """side_effect simula que se lance una excepción"""
        # En lugar de return_value, usamos side_effect para lanzar excepción
        mock_get.side_effect = requests.exceptions.Timeout("Connection timeout")

        resultado = obtener_pokemon("timeout")

        assert resultado["success"] is False
        assert "Timeout" in resultado["message"]

    @patch("pokemon.requests.get")
    def test_connection_error(self, mock_get):
        """Simulando error de conexión"""
        mock_get.side_effect = requests.exceptions.ConnectionError("No internet")

        resultado = obtener_pokemon("noconnection")

        assert resultado["success"] is False
        assert "Error de conexión" in resultado["message"]
