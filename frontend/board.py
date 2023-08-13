import pygame
from resource.color_config import ColorConfig

# 棋盤
class Board():
    def __init__(self):
        super().__init__()
        # 儲存格長度
        self.cell_len = 40
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        self.line_total_count = 15
        # 棋盤總長度
        self.board_len = self.cell_len * (self.line_total_count + 1)
        #  四角 + 中間圓點的大小，數字越大，圓越大
        self.black_circle_width = 5

    def get_surface(self) -> pygame.Surface:
        """
        獲取矩形棋盤背景物件
        """

        board = pygame.Surface(size=(self.board_len, self.board_len))
        board.fill(ColorConfig.LIGHT_YELLOW_COLOR)
        return board

    def draw_board(self, surface: pygame.Surface):
        """
        繪製棋盤
        """
        black = ColorConfig.BLACK

        # 儲存格長度
        cell_len = self.cell_len
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        line_total_count = self.line_total_count

        for i in range(1, line_total_count + 1):

            # 起始座標
            start_pos = cell_len
            # 結束座標
            end_pos = cell_len * line_total_count
            # 目前座標
            current_pos = cell_len * i
            # print(board_x_start, board_y_start, board_x_end, board_y_end)
            line_width = 1  # 寬度
            # 起始 & 最後一條線邊框加粗
            if i == 1 or i == line_total_count:
                line_width = 3
            # x 軸 橫線
            pygame.draw.line(surface, black, (start_pos, current_pos), (end_pos, current_pos), line_width)
            # y 軸  直線
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
                ColorConfig.BLACK, 
                (x * self.cell_len, y * self.cell_len),
                self.black_circle_width
            )
