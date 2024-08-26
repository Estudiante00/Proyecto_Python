from wsgiref import headers
import requests
class EmocionDetector:
    def __init__(self, api_key: str, url: str):
        self.api_key = api_key
        self.url = url

    def _validate_text(self, text: str) -> None:
        if not text.strip():
            raise ValueError("El texto no puede estar vacío")

    def detect_emocion(self, text: str) -> dict:
        self._validate_text(text)#Valida que el texto no este vacio
        #Configuracion de la solicitud a la Api de watson
        header = {
            'context-Type' : 'aplicacion/json',
            'Autorizacion' : f'portador {self.api_key}'
        }
        payload = {
            "text" : text
        }
        #Realiza solicitud a la API de Watson
        response = requests.post(self.url, headers=headers, json=payload)
        #Manejo de errores de la solicitud
        if response.status_code !=200:
            raise Exception(f"Error en la solicitud a waatson NLP: {response.status_code},{response.text}")
        #Procesa y devuelve las emociones extraidas
        return self._extract_emotions(response.json())
    def _extract_emotions(self, data: dict) -> dict:
        emociones = data.get('emocion',{}).get('documento',{}).get('emocion',{})
        return emociones
        
        