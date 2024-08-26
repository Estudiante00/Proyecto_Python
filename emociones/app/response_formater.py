class ResponseFormater:

    # incializa el constructor de la clase
    def __init__(self):
        pass

      #metodo para formatear los datos  
    def format_response(self, emotion_data: dict) -> dict:

        """
        Formatea los datos de emociones en una estructura de salida estándar.

        :param emotion_data: Diccionario con las emociones detectadas.
        :return: Diccionario formateado para la respuesta.
        """

        formatted_data = {
            "status": "success",
            "data": {
                "emotions": emotion_data
            },
            "message": "Analisis de emocion completado con exito"
        }
        return formatted_data