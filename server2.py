import os, socket, threading

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 1200))  # Railway asigna el puerto

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor escuchando en {HOST}:{PORT}")

clients = []

def handle_client(conn, addr):
    print(f"Conexión desde {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"{addr}: {data}")
            # reenviar a todos los clientes conectados
            for c in clients:
                if c != conn:
                    c.sendall(data.encode())
        except:
            break
    conn.close()
    clients.remove(conn)

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()
