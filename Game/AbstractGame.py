from Utils.Settings import Settings


class AbstractGame:
    def __init__(self, win):
        self.settings = Settings()
        self.display = win

    def start_game(self):
        pass
