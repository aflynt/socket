import socket
import threading
import pickle

HEADER = 32
FORMAT = 'utf-8'
PORT = 5050
SERVER = "192.168.0.167"
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "exit"
#HOSTNAME = socket.gethostname()
#SERVER = socket.gethostbyname( HOSTNAME )

# make a server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    msg = ''

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False

            print(f'[{addr}] {msg}')
            conn.send("got it".encode(FORMAT))
    conn.close()

def start():
    s.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


print("[STARTING] server is starting...")
start()

