import json
import random
import time
from datetime import datetime, timezone
import paho.mqtt.client as mqtt

from Config.config import MQTT_BROKER, MQTT_PORT, CA_CERT, TEMPERATURE_HUMIDITY_TOPIC

client = mqtt.Client()
client.tls_set(ca_certs=CA_CERT, certfile="temperature_humidity_sensor.cert.pem", keyfile="temperature_humidity_sensor.private.key")
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

while True:
    payload = {
        "sensor": "tempHumSensor01",
        "temperature": round(random.uniform(20.0, 28.0), 1),
        "humidity": round(random.uniform(40.0, 60.0), 1),
        "unit": {
            "temperature": "Celsius",
            "humidity": "%"
        },
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    client.publish(TEMPERATURE_HUMIDITY_TOPIC, json.dumps(payload), qos=1)
    time.sleep(10)
