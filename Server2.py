import pickle
import socket
from _thread import *

from Game.Game2Online import Game2Online

server = "192.168.1.241"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started.")

idCount = 0
games = {}


def threaded_client(conn, player, game_id):
    global idCount
    conn.send(str.encode(str(player)))

    while True:
        try:
            data = conn.recv(2048 * 4).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    print("Disconnected.")
                    break
                else:
                    pass

                conn.sendall(pickle.dumps(game))
        except:
            break

    print("Lost connection.")
    try:
        del games[game_id]
        print("Closing Game", game_id)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    player = 1
    game_id = (idCount - 1) // 2

    if idCount % 2 == 1:
        games[game_id] = Game2Online(game_id)
        print("Creating a new game...")
    else:
        games[game_id].set_ready(True)
        player = 2

    start_new_thread(threaded_client, (conn, player, game_id))
