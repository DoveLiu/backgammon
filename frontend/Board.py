import pygame
from resource.frontend_config import FrontendConfig

# 棋盤
class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 儲存格長度
        self.cell_len = 40
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        self.line_count = 15
        # 棋盤總長度
        self.board_len = self.cell_len * (self.line_count + 1 )
        # 棋盤背景色
        self.light_yellow_color = '#FFE153'
        #  四角 + 中間圓點的大小，數字越大，圓越大
        self.star_point_width = 5
    
    def get_surface(self) -> pygame.Surface:
        """
        獲取矩形棋盤背景物件
        """

        # 棋盤總長度
        board_len = self.board_len
        board_color = self.light_yellow_color

        board = pygame.Surface(size=(board_len, board_len))
        board.fill(board_color)
        return board
    
    def draw_board(self, surface:pygame.Surface):
        """
        繪製棋盤
        """
        black = 'black'

        # 儲存格長度
        cell_len = self.cell_len
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        line_count = self.line_count

        for i in range(1, line_count + 1):
            # board_x_list.append(i)
            # 起始座標
            start_pos = cell_len 
            # 結束座標
            end_pos = cell_len * line_count 
            # 目前座標
            current_pos = cell_len * i
            # print(board_x_start, board_y_start, board_x_end, board_y_end)
            line_width = 1 # 寬度
            # 起始 & 最後一條線邊框加粗
            if i == 1 or i == line_count:
                line_width = 3
            # x 軸 橫線
            pygame.draw.line(surface, black, (start_pos, current_pos), (end_pos, current_pos), line_width)  
            # y 軸  直線
            pygame.draw.line(surface, black, (current_pos, start_pos), (current_pos, end_pos), line_width)
        
    def draw_star_point(self, surface:pygame.Surface):
        """
        繪製四角四個 + 中間比較粗的圓點
        """
        
        black = 'black'

        # 儲存格長度
        cell_len = self.cell_len
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        board_line_count = self.line_count

        star_point_width = self.star_point_width

        len_4_pos = 4  * cell_len
        len_back_4_pos = (board_line_count - 3) * cell_len
        len_center_pos = ((board_line_count + 1) / 2)  * cell_len

        # 繪製比較粗的圓點清單
        star_point_pos_list = [
            (len_4_pos, len_4_pos) ,
            (len_4_pos, len_back_4_pos),
            (len_back_4_pos, len_4_pos),
            (len_back_4_pos, len_back_4_pos),
            (len_center_pos, len_center_pos)
        ]
        for i in range(len(star_point_pos_list)):
            pygame.draw.circle(surface, black, star_point_pos_list[i], star_point_width)
