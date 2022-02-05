import pickle
import socket
from _thread import *

from Game.Player2.ServerGame2 import ServerGame2

"""
The server object. It will have methods to setup the server, start the server, and a method
to perform threaded actions on each connections. They will also try to broadcast 
"""


class Server2:
    def __init__(self):
        self.server = "192.168.1.241"
        self.port = 5555

        self.idCount = 0
        self.games = {}
        self.game_instructions = {}
        self.connections = []

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.setup()
        self.startup()

    def setup(self):
        try:
            self.server_socket.bind((self.server, self.port))
        except socket.error as e:
            str(e)

    def startup(self):
        self.server_socket.listen(2)
        print("Waiting for a connection, Server Started.")

        while True:
            conn, addr = self.server_socket.accept()
            print("Connected to: ", addr)

            self.connections.append(conn)

            self.idCount += 1
            player = 1
            game_id = (self.idCount - 1) // 2

            if self.idCount % 2 == 1:
                self.games[game_id] = ServerGame2(game_id)
                self.game_instructions[game_id] = []
                print("Creating a new game...")
            else:
                self.games[game_id].set_ready(True)
                player = 2

            start_new_thread(self.threaded_client, (conn, player, game_id))

    def threaded_client(self, conn, player, game_id):
        conn.send(str.encode(str(player)))

        while True:
            try:
                data = conn.recv(2048 * 4).decode()

                if game_id in self.games:
                    game = self.games[game_id]

                    if not data:
                        print("Disconnected.")
                        break
                    elif data == "get":
                        conn.send(pickle.dumps([game, player]))
                    else:
                        pass

                    conn.sendall(pickle.dumps([game, player]))
            except:
                break

        print("Lost connection.")
        try:
            del self.games[game_id]
            print("Closing Game", game_id)
        except:
            pass

        self.idCount -= 1
        conn.close()


server = Server2()
