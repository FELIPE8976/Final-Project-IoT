import json
import random
import time
from datetime import datetime, timezone
import paho.mqtt.client as mqtt

from config import MQTT_BROKER, MQTT_PORT, MOTION_TOPIC
import os

BASE_DIR = os.path.dirname(__file__)
CA_CERT = os.path.join(BASE_DIR, "AmazonRootCA1.pem")
CERTFILE = os.path.join(BASE_DIR, "motion_sensor.cert.pem")
KEYFILE = os.path.join(BASE_DIR, "motion_sensor.private.key")

client = mqtt.Client()
client.tls_set(ca_certs=CA_CERT, certfile=CERTFILE, keyfile=KEYFILE)
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

while True:
    payload = {
        "sensor": "movSensor01",
        "motion_detected": bool(random.getrandbits(1)),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    client.publish(MOTION_TOPIC, json.dumps(payload), qos=1)
    print(f"Published to {MOTION_TOPIC}")
    time.sleep(7)
