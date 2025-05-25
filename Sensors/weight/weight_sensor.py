import json
import random
import time
from datetime import datetime, timezone
import paho.mqtt.client as mqtt

from Config.config import MQTT_BROKER, MQTT_PORT, CA_CERT, WEIGHT_TOPIC

client = mqtt.Client()
client.tls_set(ca_certs=CA_CERT, certfile="weight_sensor.cert.pem", keyfile="weight_sensor.private.key")
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

while True:
    payload = {
        "sensor": "weightSensor01",
        "value": round(random.uniform(20.0, 50.0), 2),
        "unit": "kg",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    client.publish(WEIGHT_TOPIC, json.dumps(payload), qos=1)
    time.sleep(12)
