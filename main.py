import pygame

from frontend.gomoku_gui import Gomoku_Gui


def main():
    gomoku_gui = Gomoku_Gui()
    gomoku_gui_surface = gomoku_gui.get_Surface()

    clock = gomoku_gui.pygame_clock
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gomoku_gui.draw_board(gomoku_gui_surface)
        gomoku_gui.update()

        clock.tick(60)

    gomoku_gui.end_game()


if __name__ == "__main__":
    main()
