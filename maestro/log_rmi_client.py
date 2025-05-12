# esclavo/log_rmi_client.py o maestro/log_rmi_client.py
import Pyro5.api

def enviar_log(inicio, fin, maquina, tipo, query, tiempo):
    try:
        with open("../rmi_server/log_collector.uri") as f:
            uri = f.read().strip()
        log_collector = Pyro5.api.Proxy(uri)

        entrada = f"{inicio},{fin},{maquina},{tipo},{query},{tiempo:.4f}"
        log_collector.enviar_log(entrada)

    except Exception as e:
        print(f"Error al enviar log por RMI: {e}")
