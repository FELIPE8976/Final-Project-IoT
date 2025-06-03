MQTT_BROKER = "a277byl05x37m6-ats.iot.us-east-1.amazonaws.com"
MQTT_PORT = 8883

# Global certificate (shared Amazon root CA)
CA_CERT = "AmazonRootCA1.pem"

# MQTT Topics
TEMPERATURE_HUMIDITY_TOPIC = "warehouse/zone1/temperature_humidity_sensor01/data"
MOTION_TOPIC = "warehouse/shelf3/motion_sensor01/event"
WEIGHT_TOPIC = "warehouse/loading/weight_sensor01/data"

# Sensor-specific certs and keys
TEMPERATURE_HUMIDITY_CERTFILE = "Sensors/temperature_humidity/temperature_humidity_sensor.cert.pem"
TEMPERATURE_HUMIDITY_KEYFILE = "Sensors/temperature_humidity/temperature_humidity_sensor.private.key"

MOTION_CERTFILE = "Sensors/motion/motion_sensor.cert.pem"
MOTION_KEYFILE = "Sensors/motion/motion_sensor.private.key"

WEIGHT_CERTFILE = "Sensors/weight/weight_sensor.cert.pem"
WEIGHT_KEYFILE = "Sensors/weight/weight_sensor.private.key"