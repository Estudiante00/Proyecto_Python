import os
import requests
from flask import Flask, request, jsonify, send_file
from app.emotion_detector import EmocionDetector
from app.response_formater import ResponseFormater

app = Flask(__name__)

# Ruta del archivo JSON con las credenciales de Google Cloud
credenciales_google = r"ingresa  tu API AQUI"

# Verificar si el archivo existe
if not os.path.isfile(credenciales_google):
    raise FileNotFoundError(f"El archivo de credenciales no se encuentra en la ruta: {credenciales_google}")

# Inicializa el detector de emociones con las credenciales de Google Cloud
emotion_detector = EmocionDetector(credentials_path=credenciales_google)

# Inicializa el formateador de respuestas
response_formatter = ResponseFormater()

@app.route('/emotion_detector.py', methods=['POST'])
def detectar_emocion():
    try:
        data = request.get_json()
        text = data.get('text')
        emotions = emotion_detector.detect_emocion(text)
        formatted_response = response_formatter.format_response(emotions)
        return jsonify(formatted_response)
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Error al procesar la solicitud'}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Código para hacer la solicitud POST
url = "http://127.0.0.1:5000/emotion_detector"
data = {"text": "Estoy muy feliz hoy!"}
response = requests.post(url, json=data)
print(response.json())
