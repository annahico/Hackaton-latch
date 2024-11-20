# /iot_latch_control/main.py
import flask
import requests
from flask import jsonify, request

# Configuración Latch
LATCH_APP_ID = "your_app_id"
LATCH_SECRET_KEY = "your_secret_key"
LATCH_BASE_URL = "https://latch.elevenpaths.com/api/"

# Simulación de dispositivo IoT
devices = {"light1": False, "door1": False}

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def latch_request(endpoint, params):
    # Enviar solicitud a Latch API.
    url = f"{LATCH_BASE_URL}{endpoint}"
    response = requests.post(url, params=params)
    return response.json()


@app.route('/pair', methods=['POST'])
def pair_account():
    # Vincular cuenta de Latch.
    account_id = request.json.get('account_id')
    params = {"accountId": account_id, "appId": LATCH_APP_ID}
    response = latch_request("1.0/pair", params)
    return jsonify(response)


@app.route('/control/<device_id>', methods=['POST'])
def control_device(device_id):
    # Controlar dispositivos con autenticación de Latch.
    account_id = request.json.get('account_id')
    status_response = latch_request(
        f"1.0/status/{account_id}", {"appId": LATCH_APP_ID})

    if not status_response.get('data', {}).get('operations', {}).get(LATCH_APP_ID, {}).get('status') == "on":
        return jsonify({"error": "Access Denied: Device is locked"}), 403

    action = request.json.get('action')  # 'on' o 'off'
    if device_id in devices:
        devices[device_id] = (action == 'on')
        return jsonify({"device_id": device_id, "status": devices[device_id]})
    return jsonify({"error": "Device not found"}), 404


@app.route('/status', methods=['GET'])
def device_status():
    # Obtener el estado de los dispositivos.
    return jsonify(devices)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
