# rmi_server/log_rmi_server.py
import Pyro5.api
import os
from datetime import datetime

LOG_FILE = '../logs/central_log.csv'

@Pyro5.api.expose
class LogCollector:
    def __init__(self):
        os.makedirs('../logs', exist_ok=True)
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w') as f:
                f.write("inicio,fin,maquina,tipo_maquina,query,tiempo,score,edad\n")

    def enviar_log(self, log_entry):
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry + '\n')
        print("Log recibido y guardado:", log_entry)

def main():
    daemon = Pyro5.api.Daemon()
    uri = daemon.register(LogCollector)
    print("Servidor RMI corriendo. URI:", uri)
    with open("log_collector.uri", "w") as f:
        f.write(str(uri))
    daemon.requestLoop()

if __name__ == "__main__":
    main()
