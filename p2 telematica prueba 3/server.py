# Librerias que se van a usar
import socket
from telnetlib import SE
import threading

# Cantidad de bytes para el mensaje
HEADER = 64
# Puerto que se va a utilizar
PORT = 5050
# Retonar la IP del host
SERVER = socket.gethostbyname(socket.gethostname())
# Dupla de IP y puerto
ADDR = (SERVER, PORT)
# Formato del texto
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

# Se define que permite IPv4 con protocolo TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se asocia la dupla
server.bind(ADDR)

# Funcion que conecta con el cliente
def handle_client(conn, addr):
    print(f"[New CONNECTION] {addr} connected.")
    
    # Para recibir varios mensajes se crea un ciclo
    connected = True
    while connected:
        # Se lee si hay datos
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # Si hay datos se entra al IF de lo contrario se cierra la conexion
        if msg_length:
            # Se lee el mensaje en caso de que sea para desconectarse se cierra la sesion
            # de lo contrario este se decodifica y se imprime en consola y se 
            # envia un mensaje de confirmacion al cliente
            msg_length =  int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message recieved".encode(FORMAT))
    conn.close()

# Se define una funcion para empezar  
def start():
    # Se aceptan las conexiones
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    # Se mantiente la conexion
    while True:
        # Se permite que el servidor acepte las conexiones
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
