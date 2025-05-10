from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Carga de datos locales
with open('datos/libros.json') as f:
    documentos = json.load(f)

@app.route('/buscar', methods=['GET'])
def buscar():
    termino = request.args.get('q', '').lower()
    resultados = [doc for doc in documentos if termino in doc['titulo'].lower()]
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(port=5001)  # Puerto específico para libros
