# Ruta al Python (ajusta si usas venv)
$python = "python"  # O ".\venv\Scripts\python.exe" si tienes entorno virtual

# Ejecutar script
& $python ".\Sensors\motion\motion_sensor.py" `
    --endpoint "a277byl05x37m6-ats.iot.us-east-1.amazonaws.com" `
    --ca_file ".\root-CA.crt" `
    --cert ".\Sensors\motion\Certificates\motion_sensor.cert.pem" `
    --key ".\Sensors\motion\Certificates\motion_sensor.private.key" `
    --client_id "motion_sensor" `
    --topic "warehouse/shelf3/motion_sensor01/event"