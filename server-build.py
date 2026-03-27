import socket
import threading
HEADER = 64
PORT = 5050 
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_LENGTH = conn.recv(HEADER).decode(FORMAT)
        msg_LENGTH = int(msg_LENGTH)
        msg = conn.recv(msg_LENGTH).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")
        conn.send("Msg recieved".encode(FORMAT))


    conn.close()

def start():
    server.listen()
    print(f"[SERVER] server is listening on {SERVER}")
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

print("Server is starting....")
start()





