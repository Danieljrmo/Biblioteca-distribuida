# maestro/app.py
from flask import Flask, request, jsonify
import requests
from datetime import datetime
from log_rmi_client import enviar_log
import socket

app = Flask(__name__)

# URLs de los esclavos
esclavos = {
    'libros': 'http://localhost:5001/buscar',
    'revistas': 'http://localhost:5002/buscar',
    'tesis': 'http://localhost:5003/buscar',
    'videos': 'http://localhost:5004/buscar'
}

@app.route('/query', methods=['GET'])
def query():
    inicio = datetime.now()
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


    fin = datetime.now()
    tiempo_total = (fin - inicio).total_seconds()

    enviar_log(
        inicio=inicio.isoformat(),
        fin=fin.isoformat(),
        maquina=socket.gethostname(),
        tipo='maestro',
        query='tipo_doc' if tipos else 'titulo',
        tiempo=tiempo_total,
    )
    return jsonify(resultados_ordenados)

if __name__ == '__main__':
    app.run(port=5000)
