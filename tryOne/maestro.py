from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RUTAS = {
    "libros": "http://localhost:5001/buscar",
    "articulos": "http://localhost:5002/buscar",
    "tesis": "http://localhost:5003/buscar",
    "revistas": "http://localhost:5004/buscar"
}

# Ajuste de puntaje por edad
def ajustar_por_edad(doc, edad):
    categoria = doc.get("categoria", "").lower()

    if 10 <= edad <= 15 and "ficción" in categoria:
        return 2
    elif 16 <= edad <= 30 and "tecnología" in categoria:
        return 2
    elif edad >= 31 and ("historia" in categoria or "investigación" in categoria):
        return 2
    return 0

@app.route('/query', methods=['GET'])
def buscar():
    titulo = request.args.get('titulo', '').lower()
    edad = int(request.args.get('edad', '0'))
    resultados_totales = []

    for tipo, url in RUTAS.items():
        try:
            r = requests.get(url, params={'q': titulo, edad: edad})
            resultados = r.json()
            for doc in resultados:
                doc['tipo'] = tipo
                doc['puntaje'] += ajustar_por_edad(doc, edad)
                resultados_totales.append(doc)
        except Exception as e:
            print(f"[ERROR] Falló consulta a {tipo}: {e}")

    # Ordenar por puntaje descendente
    resultados_ordenados = sorted(resultados_totales, key=lambda x: x['puntaje'], reverse=True)

    return jsonify(resultados_ordenados)

if __name__ == '__main__':
    app.run(port=5000)
