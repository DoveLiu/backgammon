from enum import Enum


class Player(Enum):
    BLACK = "black"
    WHITE = "white"


class GameState:
    def __init__(self):
        self.current_player = Player.BLACK.value

    def switch_player(self):
        if self.current_player == Player.BLACK.value:
            self.current_player = Player.WHITE.value
        else:
            self.current_player = Player.BLACK.value
