import pygame
from frontend.board import Board
from resource.frontend_config import FrontendConfig

# 遊戲介面
class Gui(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # pygame.init()

    def get_Surface (self) -> pygame.Surface:
        """
        獲取矩形遊戲介面物件
        """

        high = FrontendConfig.GUI_HIGH
        width = FrontendConfig.GUI_WIDTH
        color = FrontendConfig.GUI_COLOR
        
        screen = pygame.display.set_mode((width, high))
        screen.fill(color)
        return screen
    
    def draw_board(self, gui_surface:pygame.Surface, board_surface:pygame.Surface):
        """
        把棋盤矩形物件，繪製到遊戲介面矩形物件上
        """
        
        gui_high = FrontendConfig.GUI_HIGH
        gui_width = FrontendConfig.GUI_WIDTH
        board_len = FrontendConfig.BOARD_LEN

        board_init_width = (gui_width - board_len) / 2 
        borad_init_high = (gui_high - board_len) / 2
        # 要把 Surface 元素畫在哪，目前置中
        gui_surface.blit(board_surface, (board_init_width, borad_init_high))
    