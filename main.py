import pygame

from frontend.gomoku_gui import Gomoku_Gui


def main():
    # 繪製圖形化介面
    gomoku_gui = Gomoku_Gui()
    gomoku_gui_surface = gomoku_gui.get_Surface()

    clock = gomoku_gui.pygame_clock
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 把棋盤繪製到遊戲介面上
        gomoku_gui.draw_board(gomoku_gui_surface)

        # 更新遊戲畫面
        gomoku_gui.update()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        clock.tick(60)

    gomoku_gui.end_game()


if __name__ == "__main__":
    main()
