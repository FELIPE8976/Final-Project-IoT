# Ruta al Python (ajusta si usas venv)
$python = "python"  # O ".\venv\Scripts\python.exe" si tienes entorno virtual

# Ejecutar script
& $python ".\Sensors\temperature_humidity\temperature_humidity_sensor.py" `
    --endpoint "a277byl05x37m6-ats.iot.us-east-1.amazonaws.com" `
    --ca_file ".\root-CA.crt" `
    --cert ".\Sensors\temperature_humidity\Certificates\temperature_humidity_sensor.cert.pem" `
    --key ".\Sensors\temperature_humidity\Certificates\temperature_humidity_sensor.private.key" `
    --client_id "temperature_humidity" `
    --topic "warehouse/zone1/temperature_humidity_sensor01/data"