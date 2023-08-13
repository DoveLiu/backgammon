import pygame
from resource.color_config import ColorConfig

# 棋盤
class Board():
    def __init__(self):
        super().__init__()
        self.cell_len = 40
        self.line_count = 15
        self.total_len = self.cell_len * (self.line_count + 1)
        self.black_circle_width = 5

    def get_surface(self) -> pygame.Surface:
        """
        獲取矩形棋盤背景物件
        """

        board = pygame.Surface(size=(self.total_len, self.total_len))
        board.fill(ColorConfig.LIGHT_YELLOW_COLOR.value)
        return board

    def draw_board(self, surface: pygame.Surface):
        """
        繪製棋盤
        """
        black = ColorConfig.BLACK.value

        cell_len = self.cell_len
        line_total_count = self.line_count

        for i in range(1, line_total_count + 1):

            start_pos = cell_len
            end_pos = cell_len * line_total_count
            current_pos = cell_len * i
            line_width = 1  
            if i == 1 or i == line_total_count:
                line_width = 3
            # x 軸 
            pygame.draw.line(surface, black, (start_pos, current_pos), (end_pos, current_pos), line_width)
            # y 軸  
            pygame.draw.line(surface, black, (current_pos, start_pos), (current_pos, end_pos), line_width)

    def draw_black_circle(self, surface: pygame.Surface):
        """
        繪製四角四個 + 中間比較粗的圓點
        """

        black_circle_pos_list = [
            (4, 4),
            (4, 12),
            (12, 4),
            (12, 12),
            (8, 8),
        ]

        for pos in black_circle_pos_list:
            x, y = pos
            pygame.draw.circle(
                surface,
                ColorConfig.BLACK.value, 
                (x * self.cell_len, y * self.cell_len),
                self.black_circle_width
            )
