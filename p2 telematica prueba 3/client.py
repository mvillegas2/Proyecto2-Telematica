import socket

###Primero declaramos las varaibles estaticas que van ligadas a la conectividad y a las generalidades del codigo###
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "192.168.39.133"
ADDR = (SERVER, PORT)

### especificamos al socket los tipos de direccion que se van a estar utilizando ###
### y tambien estamos indicando que estamos transmitiendo data a traves del socket ###
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

### ###
def send(msg):
    ### codificamos el mensaje de string a bytes para poder enviarlo a traves del socket ###
    message = msg.encode(FORMAT)
    ### Luego tambien enviamos la longitud del mensaje que queremos enviar pero lo mandamos a traves###
    ### de bytes luego de convertirlo en string y codificarlo###
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    ### Por ultimo se envia la longitud del mensaje y el mensaje al servidor ###
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

### Enviamos los mensajes que queramos mandar al servidor para esperar una respuesta de confirmacion###
send("Prueba envio 1")
input()
send("prueba envio 2")
input()
send("prueba envio 3")
input()

###Por ultimo enviamos el mensaje de desconexion luego de haber enviado todos los mensajes que requeriamos###
send(DISCONNECT_MESSAGE)


