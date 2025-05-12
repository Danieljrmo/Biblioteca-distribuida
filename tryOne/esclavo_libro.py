from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Carga base de datos local
with open('libros.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

@app.route('/buscar', methods=['GET'])
def buscar():
    termino = request.args.get('q', '').lower()
    edad = int(request.args.get('edad', 0))
    palabras = termino.split()

    resultados = []

    for doc in datos:
        titulo = doc['titulo'].lower()
        coincidencias = sum(1 for palabra in palabras if palabra in titulo)

        # Nuevo filtro por edad mínima
        if coincidencias > 0 and edad >= doc.get('edad_minima', 0):
            doc_resultado = {
                "id": doc['id'],
                "titulo": doc['titulo'],
                "categoria": doc['categoria'],
                "puntaje": coincidencias
            }
            resultados.append(doc_resultado)

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(port=5001)

