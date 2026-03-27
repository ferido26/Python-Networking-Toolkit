import socket

HEADER = 64
PORT = 5050 
FORMAT = "utf-8"
SERVER = "192.168.31.185"
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_LENGTH = len(message)
    send_length = str(msg_LENGTH).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("HELLO WORLD!")
input()
send("HELLO FERIDO")
input()
send("HELLO TIM")

send(DISCONNECT_MESSAGE)