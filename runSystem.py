# run_sistema.py
import subprocess
import time
import os
import sys

def launch_process(path, filename):
    return subprocess.Popen([sys.executable, filename], cwd=path)

def main():
    # Ruta base (ajusta según tu estructura si es distinta)
    base_dir = os.path.abspath(os.path.dirname(__file__))

    print("➡️ Iniciando Servidor RMI...")
    rmi_path = os.path.join(base_dir, 'rmi_server')
    rmi_server = launch_process(rmi_path, 'log_rmi_server.py')
    time.sleep(2)  # Espera para asegurar que se levante

    print("➡️ Iniciando nodos esclavos...")
    esclavos_path = os.path.join(base_dir, 'esclavos')
    esclavos = launch_process(esclavos_path, 'runEsclavos.py')
    time.sleep(3)  # Dar tiempo a que levanten los esclavos

    print("➡️ Iniciando maestro...")
    maestro_path = os.path.join(base_dir, 'maestro')
    maestro = launch_process(maestro_path, 'app.py')

    print("✅ Todo el sistema está en ejecución.")
    print("ℹ️ Usa CTRL+C para detener manualmente los procesos.")

    try:
        maestro.wait()
    except KeyboardInterrupt:
        print("\n🛑 Terminando procesos...")
        for proc in [rmi_server, esclavos, maestro]:
            proc.terminate()
        print("✅ Todos los procesos han sido detenidos.")

if __name__ == '__main__':
    main()
