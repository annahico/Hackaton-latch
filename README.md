# **IoT Control System with Latch Authentication**

### **Descripción**

Este proyecto implementa un sistema de control de dispositivos IoT utilizando la API de Latch para autenticar y proteger el acceso. Los usuarios pueden vincular su cuenta de Latch, controlar dispositivos (como luces o puertas) y verificar su estado en tiempo real.

---

## **Características**

- **Autenticación Segura**: Integración con Latch para gestionar permisos y autenticación de dispositivos IoT.
- **Control de Dispositivos IoT**: Permite encender, apagar o bloquear dispositivos simulados.
- **Simulación MQTT**: Comunicación con dispositivos IoT simulados mediante MQTT.
- **Registro de Eventos**: Registra acciones en un archivo de log para auditoría.

---

## **Tecnologías Utilizadas**

- **Backend**: Python con Flask.
- **Autenticación**: API de Latch.
- **Simulación IoT**: MQTT (usando `paho-mqtt`).
- **Frontend (Opcional)**: Plantillas HTML con Flask.

---

## **Estructura del Proyecto**

```plaintext
iot_latch_control/
│
├── main.py                 # Archivo principal de la aplicación Flask
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno (App ID y Secret Key)
├── README.md               # Documentación del proyecto
│
├── static/                 # Archivos estáticos (opcional para interfaz web)
│   ├── css/
│   │   └── styles.css      # Estilos CSS
│   └── js/
│       └── scripts.js      # Scripts JavaScript
│
├── templates/              # Plantillas HTML para la interfaz web
│   └── index.html          # Página principal
│
├── mqtt_client/            # Simulación de dispositivos IoT
│   ├── __init__.py         # Inicializador del módulo
│   └── device_simulator.py # Simulador de dispositivos MQTT
│
└── logs/                   # Carpeta para registros
    └── app.log             # Log del sistema
```
