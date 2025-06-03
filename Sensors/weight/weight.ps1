# Ruta al Python (ajusta si usas venv)
$python = "python"  # O ".\venv\Scripts\python.exe" si tienes entorno virtual

# Ejecutar script
& $python ".\Sensors\weight\weight_sensor.py" `
    --endpoint "a277byl05x37m6-ats.iot.us-east-1.amazonaws.com" `
    --ca_file ".\root-CA.crt" `
    --cert ".\Sensors\weight\Certificates\weight_sensor.cert.pem" `
    --key ".\Sensors\weight\Certificates\weight_sensor.private.key" `
    --client_id "weight_sensor" `
    --topic "warehouse/shelf3/weight_sensor01/event"