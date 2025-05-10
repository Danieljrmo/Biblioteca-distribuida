from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Diccionario de rutas por tipo
RUTAS = {
    "libros": "http://localhost:5001/buscar",
    "articulos": "http://localhost:5002/buscar",
    "tesis": "http://localhost:5003/buscar",
    "revistas": "http://localhost:5004/buscar"
}

@app.route('/buscar', methods=['GET'])
def buscar():
    tipo = request.args.get('tipo')
    termino = request.args.get('q')
    
    if tipo not in RUTAS:
        return jsonify({"error": "Tipo de documento no válido"}), 400
    
    try:
        respuesta = requests.get(RUTAS[tipo], params={'q': termino})
        return jsonify(respuesta.json())
    except requests.exceptions.RequestException:
        return jsonify({"error": "No se pudo contactar al nodo esclavo"}), 500

if __name__ == '__main__':
    app.run(port=5000)  # Nodo maestro en el puerto 5000
