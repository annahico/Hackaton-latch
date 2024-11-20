// URL base de la API
const BASE_URL = "http://127.0.0.1:5000";

// Función para obtener el estado de los dispositivos
async function fetchDeviceStatus() {
    const response = await fetch(`${BASE_URL}/status`);
    const devices = await response.json();
    renderDevices(devices);
}

// Función para renderizar la lista de dispositivos
function renderDevices(devices) {
    const deviceList = document.getElementById("device-list");
    deviceList.innerHTML = ""; // Limpiar lista anterior

    Object.entries(devices).forEach(([device, status]) => {
        const deviceElement = document.createElement("div");
        deviceElement.textContent = `${device}: ${status ? "Encendido" : "Apagado"}`;
        deviceList.appendChild(deviceElement);
    });
}

// Función para controlar un dispositivo
async function controlDevice(event) {
    event.preventDefault(); // Evitar recarga de página

    const deviceId = document.getElementById("device-id").value;
    const action = document.getElementById("action").value;

    const response = await fetch(`${BASE_URL}/control/${deviceId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ account_id: "your_account_id", action }),
    });

    const message = await response.json();
    const controlMessage = document.getElementById("control-message");

    if (response.ok) {
        controlMessage.textContent = `Dispositivo ${deviceId} actualizado correctamente.`;
        fetchDeviceStatus(); // Actualizar la lista de dispositivos
    } else {
        controlMessage.textContent = `Error: ${message.error}`;
    }
}

// Configurar eventos al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    fetchDeviceStatus(); // Obtener estado inicial de dispositivos

    // Configurar el formulario de control
    const controlForm = document.getElementById("control-form");
    controlForm.addEventListener("submit", controlDevice);
});
