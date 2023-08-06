import pygame

from frontend.gui import Gui


def main():
    # 繪製圖形化介面
    gui = Gui()
    gui_surface = gui.get_Surface()

    clock = gui.pygame_clock
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 把棋盤繪製到遊戲介面上
        gui.draw_board(gui_surface)

        # 更新遊戲畫面
        gui.update()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        clock.tick(60)

    gui.end_game()


if __name__ == "__main__":
    main()
