import pygame


# 棋盤
class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 儲存格長度
        self.cell_len = 40
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        self.line_total_count = 15
        # 棋盤總長度
        self.board_len = self.cell_len * (self.line_total_count + 1)
        # 棋盤背景色
        self.light_yellow_color = "#FFE153"
        #  四角 + 中間圓點的大小，數字越大，圓越大
        self.black_circle_width = 5

    def get_surface(self) -> pygame.Surface:
        """
        獲取矩形棋盤背景物件
        """

        # 棋盤總長度
        board_len = self.board_len

        board = pygame.Surface(size=(board_len, board_len))
        board.fill(self.light_yellow_color)
        return board

    def draw_board(self, surface: pygame.Surface):
        """
        繪製棋盤
        """
        black = "black"

        # 儲存格長度
        cell_len = self.cell_len
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        line_total_count = self.line_total_count

        for i in range(1, line_total_count + 1):
            # board_x_list.append(i)
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

        # # 儲存格長度
        # cell_len = self.cell_len
        # # 棋盤線條數量 ( 幾乘幾的棋盤 )
        # board_line_count = self.line_total_count

        # len_4_pos = 4 * cell_len # 160
        # len_back_4_pos = (board_line_count - 3) * cell_len # 480
        # len_center_pos = ((board_line_count + 1) / 2) * cell_len # 320
        # print('len_4_pos: ', len_4_pos)
        # print('len_back_4_pos', len_back_4_pos)
        # print('len_center_pos', len_center_pos)
        # # 繪製比較粗的圓點清單
        # star_point_pos_list = [
        #     (len_4_pos, len_4_pos),
        #     (len_4_pos, len_back_4_pos),
        #     (len_back_4_pos, len_4_pos),
        #     (len_back_4_pos, len_back_4_pos),
        #     (len_center_pos, len_center_pos),
        # ]
        black = "black"
        black_circle_width = self.black_circle_width

        black_circle_pos_list = [
            (160, 160),
            (160, 480),
            (480, 160),
            (480, 480),
            (320, 320),
        ]

        for i in range(len(black_circle_pos_list)):
            pygame.draw.circle(surface, black, black_circle_pos_list[i], black_circle_width)
