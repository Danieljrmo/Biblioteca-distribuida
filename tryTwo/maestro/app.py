# maestro/app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URLs de los esclavos
esclavos = {
    'libro': 'http://localhost:5001/buscar',
    'video': 'http://localhost:5002/buscar',
    'tesis': 'http://localhost:5003/buscar',
    'revista': 'http://localhost:5004/buscar'
}

@app.route('/query', methods=['GET'])
def query():
    titulo = request.args.get('titulo', '').lower()
    tipos = request.args.get('tipo_doc', '').lower().split()
    edad = request.args.get('edad', '')
    resultados_totales = []

    if titulo:
        # Búsqueda por título: consultar todos los esclavos
        for esclavo_url in esclavos.values():
            try:
                r = requests.get(esclavo_url, params={'titulo': titulo, 'edad': edad})
                if r.status_code == 200:
                    resultados_totales.extend(r.json())
            except Exception as e:
                print(f"Error al consultar esclavo {esclavo_url}: {e}")
    elif tipos:
        # Búsqueda por tipo_doc: consultar solo los esclavos correspondientes
        for tipo in tipos:
            esclavo_url = esclavos.get(tipo)
            if esclavo_url:
                try:
                    r = requests.get(esclavo_url, params={'edad': edad})
                    if r.status_code == 200:
                        resultados_totales.extend(r.json())
                except Exception as e:
                    print(f"Error al consultar esclavo {esclavo_url}: {e}")

    # Ordenar por ranking (de mayor a menor)
    resultados_ordenados = sorted(resultados_totales, key=lambda x: x.get('ranking', 0), reverse=True)

    return jsonify(resultados_ordenados)

if __name__ == '__main__':
    app.run(port=5000)
