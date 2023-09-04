from resource.color import Color

import pygame

from frontend.board import Board
from frontend.game_state import GameState


class GoStone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 15
        self.init_pos_hight = 45
        self.init_pos_width = 325
        self.status = "transparent"

        self.transparent_image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self._draw_go_stone(self.transparent_image, (0, 0, 0, 0))

        self.white_image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self._draw_go_stone(self.white_image, Color.WHITE.value)

        self.black_image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self._draw_go_stone(self.black_image, Color.BLACK.value)

        self.image = self.transparent_image
        self._change_color()
        board = Board()
        pos_y = self.y * board.cell_len + self.init_pos_width
        pos_x = self.x * board.cell_len + self.init_pos_hight
        self.rect = self.image.get_rect(center=(pos_y, pos_x))

    def _draw_go_stone(self, image, color):
        pygame.draw.circle(image, color, (self.width, self.width), self.width)

    def _change_color(self):
        match self.status:
            case "transparent":
                self.image = self.transparent_image
            case "white":
                self.image = self.white_image
            case "black":
                self.image = self.black_image
            case _:
                print("change color error")

    def update(self, event_list: list, game_state: GameState):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # print(self.x, self.y)
                    if self.status == "transparent":
                        self.status = game_state.current_player
                        game_state.switch_player()
                        self._change_color()
