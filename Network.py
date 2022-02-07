import socket
import pickle
import time


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.setblocking(False)
        # self.server = "192.168.1.241"
        self.server = 'localhost'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()
        # self.client.settimeout(0.1)

    def get_player(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048 * 4).decode()
        except:
            pass

    def send2(self, data):
        try:
            self.client.sendall(str.encode(data))

            return pickle.loads(self.client.recv(2048 * 32))
        except socket.error as e:
            print(e)

    def recvall(self):
        BUFF_SIZE = 2048 * 4

        fragments = []
        while True:
            try:
                chunk = self.client.recv(BUFF_SIZE)
            except socket.error:
                break
            else:
                if not chunk:
                    break
                fragments.append(chunk)

        return_data = b''.join(fragments)

        return pickle.loads(return_data)

    def get_socket(self):
        return self.client
