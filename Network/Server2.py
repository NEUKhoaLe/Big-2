import socket
from _thread import *

server = "192.168.1.241"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started.")

idCount = 0


def threaded_client(conn, player, game_id):
    conn.send(str.encode("Connected"))
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected.")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection.")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    player = 0
    game_id = (idCount - 1) // 2

    if idCount % 2 == 1:
        # games[game_id] =
        pass
    else:
        pass

    start_new_thread(threaded_client, (conn, player, game_id))
