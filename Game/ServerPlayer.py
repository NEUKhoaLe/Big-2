from Utils.ServerSettings import ServerSettings


class ServerPlayer:
    def __init__(self, player_type="", name=""):
        self.name = name
        self.score = 0
        self.player_type = player_type
        self.settings = ServerSettings()

    def get_name(self):
        return self.name

    def enter_name(self, name):
        self.name = name

    def enter_score(self, score):
        self.score = score
