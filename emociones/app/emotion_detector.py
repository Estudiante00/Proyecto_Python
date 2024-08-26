from google.cloud import language_v1
import os

class EmocionDetector:
    def __init__(self, credentials_path: str):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        self.client = language_v1.LanguageServiceClient()

    def _validate_text(self, text: str) -> None:
        if not text.strip():
            raise ValueError("El texto no puede estar vacío")

    def detect_emocion(self, text: str) -> dict:
        self._validate_text(text)

        # Preparar el documento para la API de Google Cloud
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

        # Hacer la solicitud a la API
        response = self.client.analyze_sentiment(document=document)
        sentiment = response.document_sentiment

        # Devolver el resultado en un formato adecuado
        return {
            "score": sentiment.score,
            "magnitude": sentiment.magnitude
        }
