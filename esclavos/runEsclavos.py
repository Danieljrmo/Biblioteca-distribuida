import subprocess

# Lista de rutas o comandos para iniciar los esclavos
esclavos = [
    "python libros.py",
    "python revistas.py",
    "python tesis.py",
    "python videos.py"
]

procesos = []

try:
    # Iniciar cada esclavo
    for esclavo in esclavos:
        print(f"Iniciando: {esclavo}")
        proceso = subprocess.Popen(esclavo, shell=True)
        procesos.append(proceso)

    # Esperar a que todos los procesos terminen (opcional)
    for proceso in procesos:
        proceso.wait()

except KeyboardInterrupt:
    print("\nDeteniendo todos los esclavos...")
    for proceso in procesos:
        proceso.terminate()
    print("Todos los esclavos han sido detenidos.")