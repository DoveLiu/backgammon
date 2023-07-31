import pygame
from resource.frontend_config import FrontendConfig
from frontend.board import Board
from frontend.gui import Gui

# pygame setup
pygame.init()

# 繪製圖形化介面
gui = Gui()
gui_surface = gui.get_Surface()

clock = pygame.time.Clock()
running = True
dt = 0

# 繪製棋盤相關操作
board = Board()
board_surface = board.get_surface()
board.draw_board(board_surface)
board.draw_star_point(board_surface)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 把棋盤繪製到遊戲介面上
    gui.draw_board(gui_surface, board_surface)

    # flip() the display to put your work on screen
    # pygame.display.flip()
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()