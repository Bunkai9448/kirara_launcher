import requests

JISHO_URL = "https://jisho.org/api/v1/search/words"

def jisho_Dic(texto):
 try:
  parametro = {"keyword": texto}
  response = requests.get(JISHO_URL, params=parametro, timeout=5)

  # Error en conexion
  if response.status_code != 200:
   return "Error en la consulta de Jisho."

  # No hay datos para el texto
  data = response.json()
  if not data["data"]:
   return "No se han obtenido equivalencias al texto"

  # Guarda los datos obtenidos
  result = data["data"][0]
  palabra = result["japanese"][0].get("word","")
  lectura = result["japanese"][0].get("reading","")
  significado = ", " .join(result["senses"][0]["english_definitions"])

  # Devuelve los datos obtenidos
  return f"{palabra} ({lectura})\nTrad: {significado}"

 except Exception as e:
  return f"Error: {str(e)}"
