"""
Cliente simple para la API de Pokemon.
Solo extrae name y order de un pokemon.
"""
import requests


def obtener_pokemon(nombre):
    """
    Obtiene información básica de un Pokemon.
    
    Args:
        nombre (str): Nombre del pokemon (ej: "ditto", "pikachu")
    
    Returns:
        dict: {"name": str, "order": int, "success": bool, "message": str}
    """
    if not nombre:
        return {
            "success": False,
            "message": "El nombre del pokemon es requerido",
            "name": None,
            "order": None
        }
    
    try:
        # Llamada a la API real de Pokemon
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "message": f"Pokemon {nombre} encontrado",
                "name": data["name"],
                "order": data["order"]
            }
        elif response.status_code == 404:
            return {
                "success": False,
                "message": f"Pokemon '{nombre}' no encontrado",
                "name": None,
                "order": None
            }
        else:
            return {
                "success": False,
                "message": f"Error de la API: {response.status_code}",
                "name": None,
                "order": None
            }
            
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "message": "Timeout: La API no responde",
            "name": None,
            "order": None
        }
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "message": "Error de conexión con la API",
            "name": None,
            "order": None
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error inesperado: {str(e)}",
            "name": None,
            "order": None
        } 