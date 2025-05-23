# esclavo/libros.py
from flask import Flask, request, jsonify
import json
from datetime import datetime
from log_rmi_client import enviar_log
import socket

app = Flask(__name__)

# Cargar solo libros
with open('../datos/tesis.json', 'r') as f:
    datos = json.load(f)

def obtener_preferencia_por_edad(edad):
    if 10 <= edad <= 15:
        return 'ciencia ficción'
    elif 16 <= edad <= 25:
        return 'tecnología'
    else:
        return 'historia'

@app.route('/buscar', methods=['GET'])

def buscar():
    inicio = datetime.now()
    titulo = request.args.get('titulo', '').lower()
    edad_str = request.args.get('edad')
    terminos = titulo.split()
    resultados = []

    try:
        edad = int(edad_str) if edad_str else None
    except:
        edad = None

    preferencia = obtener_preferencia_por_edad(edad) if edad else None

    for doc in datos:
        coincidencias = sum(1 for t in terminos if t in doc['titulo'].lower())
        ranking = coincidencias

        # Aumentar ranking si coincide con el género favorito del grupo etario
        if edad and 'genero' in doc and preferencia:
            if preferencia.lower() in doc['genero'].lower():
                ranking += 2  # o cualquier peso que estimes adecuado

        if titulo == '' or coincidencias > 0:
            doc_copy = doc.copy()
            doc_copy['ranking'] = ranking
            resultados.append(doc_copy)

    fin = datetime.now()
    tiempo_total = (fin - inicio).total_seconds()
    ## pasar tiempo_total a milisegundos
    tiempo_total = round(tiempo_total * 1000, 2)

    enviar_log(
        inicio=inicio.isoformat(),
        fin=fin.isoformat(),
        maquina=socket.gethostname(),
        tipo='esclavo',
        query='tesis',
        tiempo=tiempo_total
    )

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(port=5003)