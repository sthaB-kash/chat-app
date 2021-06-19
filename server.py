import socket
import threading
import time

HEADER = 64
PORT = 1229

# SERVER = "192.168.123.2"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[New connection] { addr } connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode('utf-8')
        if msg_length:
            # print("length",msg_length)
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            # print("**********",msg)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode("utf-8"))
    print("outside loop(server)")
    conn.close()


def start():
    server.listen()
    print(f"[LItSTENING] server is Listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE Connections] {threading.activeCount()-1}")

# print(server.listen())


print("[STARTING] server is starting...")

start()