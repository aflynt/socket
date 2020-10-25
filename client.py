import socket
import pickle

#HEADERSIZE = 10
HEADER = 32
FORMAT = 'utf-8'
PORT = 5050
SERVER = "192.168.0.167"
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "exit"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

def send(msg):
    msg = msg.encode(FORMAT)
    hdr_msg = bytes(f'{len(msg):<{HEADER}}',FORMAT)

    s.send(hdr_msg)
    s.send(msg)
    print(s.recv(2048).decode())

send("Hello, Austin!")
input()
send("Hello, from me!")
input()
send("Hello, again me!")
send(DISCONNECT_MSG)
