# Ruta a Python (ajústala si estás usando un venv)
$python = "python"  # O ".\venv\Scripts\python.exe" si usas entorno virtual

# Ejecutar el script con parámetros
& $python ".\subscriber.py" `
    --endpoint "a277byl05x37m6-ats.iot.us-east-1.amazonaws.com" `
    --ca_file "root-CA.crt" `
    --cert "subscriber.cert.pem" `
    --key "subscriber.private.key" `
    --client_id "subscriber" `