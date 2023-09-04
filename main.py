import pygame

from frontend.game_state import GameState
from frontend.go_stone import GoStone
from frontend.gomoku_gui import Gomoku_Gui


def main():
    gomoku_gui = Gomoku_Gui()
    gomoku_gui_surface = gomoku_gui.get_surface()
    gomoku_gui.draw_board(gomoku_gui_surface)

    go_stone_group = pygame.sprite.Group()
    for x, y in gomoku_gui.get_go_stone_pos_list():
        go_stone = GoStone(x, y)
        go_stone_group.add(go_stone)

    game_state = GameState()
    clock = gomoku_gui.pygame_clock
    running = True

    while running:
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

        go_stone_group.draw(gomoku_gui_surface)
        go_stone_group.update(event_list, game_state)
        gomoku_gui.update()

        clock.tick(60)

    gomoku_gui.end_game()


if __name__ == "__main__":
    main()
