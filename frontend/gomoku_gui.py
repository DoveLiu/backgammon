import pygame

from frontend.board import Board
from resource.color_config import ColorConfig

# 遊戲介面
class Gomoku_Gui():
    def __init__(self):
        super().__init__()
        pygame.init()
        self.high = 720
        self.width = 1280
        self.pygame_clock = pygame.time.Clock()

        board_surface = self.board_init()
        self.board_surface = board_surface

    def board_init(self) -> pygame.Surface:
        """
        初始化繪製棋盤相關操作
        """
        board = Board()
        board_surface = board.get_surface()
        board.draw_board(board_surface)
        board.draw_black_circle(board_surface)
        return board_surface

    def get_Surface(self) -> pygame.Surface:
        """
        獲取矩形遊戲介面物件
        """

        screen = pygame.display.set_mode((self.width, self.high))
        screen.fill(ColorConfig.LIGHT_GRAY_COLOR)
        return screen

    def draw_board(self, gui_surface: pygame.Surface):
        """
        把棋盤矩形物件，繪製到遊戲介面矩形物件上
        """
        board = Board()

        board_init_width = (self.width - board.total_len) / 2
        board_init_high = (self.high - board.total_len) / 2
        gui_surface.blit(self.board_surface, (board_init_width, board_init_high))

    def update(self):
        """
        更新遊戲畫面
        """
        pygame.display.update()

    def end_game(self):
        pygame.quit()
