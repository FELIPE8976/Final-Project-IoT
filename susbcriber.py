from awscrt import mqtt, http
from awsiot import mqtt_connection_builder
import sys
import threading
import json

from datetime import datetime

received_all_event = threading.Event()

# Callbacks de conexión
def on_connection_interrupted(connection, error, **kwargs):
    print(f"Connection interrupted: {error}")

def on_connection_resumed(connection, return_code, session_present, **kwargs):
    print(f"Connection resumed: return_code={return_code}, session_present={session_present}")
    if return_code == mqtt.ConnectReturnCode.ACCEPTED and not session_present:
        print("Session not persisted. Resubscribing...")
        resubscribe_future, _ = connection.resubscribe_existing_topics()
        resubscribe_future.add_done_callback(on_resubscribe_complete)

def on_resubscribe_complete(resubscribe_future):
    resubscribe_results = resubscribe_future.result()
    print(f"Resubscribe results: {resubscribe_results}")
    for topic, qos in resubscribe_results['topics']:
        if qos is None:
            sys.exit(f"Server rejected resubscribe to topic: {topic}")

# Callback al recibir mensajes
def on_message_received(topic, payload, **kwargs):
    print(f"\nMensaje recibido en topic '{topic}':")
    print(json.loads(payload))

if __name__ == "__main__":
    # Crear conexión MQTT
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint="a277byl05x37m6-ats.iot.us-east-1.amazonaws.com",
        port=8883,
        cert_filepath="./Certificates/subscriber.cert.pem",
        pri_key_filepath="./Certificates/subscriber.private.key",
        ca_filepath="root-CA.crt",
        client_id="subscriber_client",
        clean_session=False,
        keep_alive_secs=30,
        http_proxy_options=None,
        on_connection_interrupted=on_connection_interrupted,
        on_connection_resumed=on_connection_resumed
    )

    print(f"Conectando al endpoint con client ID ...")
    mqtt_connection.connect().result()
    print("Conectado.")

    # Lista de topics
    topics = [
        "warehouse/zone1/temperature_humidity_sensor01/data",
        "warehouse/shelf3/motion_sensor01/event",
        "warehouse/loading/weight_sensor01/data"
    ]

    # Subscribirse a cada topic
    for topic in topics:
        print(f"Suscribiéndose a '{topic}'...")
        subscribe_future, _ = mqtt_connection.subscribe(
            topic=topic,
            qos=mqtt.QoS.AT_LEAST_ONCE,
            callback=on_message_received
        )
        subscribe_future.result()
        print(f"Subscrito a: {topic}")

    # Mantener el script en ejecución
    print("\nEsperando mensajes. Presiona Ctrl+C para salir.")
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        print("\nDesconectando...")
        mqtt_connection.disconnect().result()
        print("Desconectado.")
