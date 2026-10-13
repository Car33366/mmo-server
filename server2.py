import os
import socket

# Railway asigna el puerto en la variable de entorno PORT
PORT = int(os.environ.get("PORT", 12345))  # usa 12345 si no existe PORT
HOST = "0.0.0.0"  # escucha en todas las interfaces

# Crear socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permitir reusar el puerto si se reinicia rápido
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Asociar el socket al host y puerto
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    # Esperar conexión de cliente
    client_socket, addr = server_socket.accept()
    print(f"Conexión desde {addr}")

    try:
        # Recibir datos del cliente
        data = client_socket.recv(1024).decode("utf-8").strip()
        if data:
            print(f"Cliente dice: {data}")

        # Enviar respuesta terminada en \0 (necesario para Flash AS2)
        mensaje = "Hola desde el servidor en Railway!\0"
        client_socket.send(mensaje.encode("utf-8"))

    except Exception as e:
        print(f"Error: {e}")

    # Cerrar conexión
    client_socket.close()
