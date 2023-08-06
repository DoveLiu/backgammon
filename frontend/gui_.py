import pygame

from frontend.board import Board


# 遊戲介面
class Gui(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.high = 720
        self.width = 1280
        self.light_gray_color = "#F0F0F0"
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
        board.draw_star_point(board_surface)
        return board_surface

    def get_Surface(self) -> pygame.Surface:
        """
        獲取矩形遊戲介面物件
        """

        high = self.high
        width = self.width
        light_gray_color = self.light_gray_color

        screen = pygame.display.set_mode((width, high))
        screen.fill(light_gray_color)
        return screen

    def draw_board(self, gui_surface: pygame.Surface):
        """
        把棋盤矩形物件，繪製到遊戲介面矩形物件上
        """
        board = Board()

        gui_high = self.high
        gui_width = self.width
        board_len_count = board.board_len_count

        board_surface = self.board_surface

        board_init_width = (gui_width - board_len_count) / 2
        board_init_high = (gui_high - board_len_count) / 2
        # 要把 Surface 元素畫在哪，目前置中
        gui_surface.blit(board_surface, (board_init_width, board_init_high))

    def update(self):
        """
        更新遊戲畫面
        """
        pygame.display.update()

    def end_game(self):
        pygame.quit()
