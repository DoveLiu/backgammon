import pygame
from resource.FrontendConfig import FrontendConfig

# 棋盤
class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
    def get_Surface(self) -> pygame.Surface:
        """
        獲取矩形棋盤背景物件
        """

        # 棋盤總長度
        board_len = FrontendConfig.BOARD_LEN
        board_color = FrontendConfig.BOARD_COLOR

        board = pygame.Surface(size=(board_len, board_len))
        board.fill(board_color)
        return board
    
    def draw_board(self, surface:pygame.Surface):
        """
        繪製棋盤
        """

        black = FrontendConfig.BLACK
        # 儲存格長度
        cell_len = FrontendConfig.CELL_LEN
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        line_count = FrontendConfig.LINE_COUNT

        # 總共 15 行
        for i in range(1, line_count + 1):
            # board_x_list.append(i)
            # 起始座標
            board_start = cell_len 
            board_start_i = cell_len * i
            # 結束座標
            board_end = cell_len * line_count 
            board_end_i = cell_len * i
            # print(board_x_start, board_y_start, board_x_end, board_y_end)
            line_width = 1 # 寬度
            if i == 1 or i == line_count:
                line_width = 3
            # x 軸 橫線
            pygame.draw.line(surface, black, (board_start, board_start_i), (board_end, board_end_i), line_width)  
            # y 軸  直線
            pygame.draw.line(surface, black, (board_start_i, board_start), (board_end_i, board_end), line_width)
        
    def draw_star_point(self, surface:pygame.Surface):
        """
        繪製四角四個 + 中間比較粗的圓點
        """
        
        black = FrontendConfig.BLACK

        # 儲存格長度
        cell_len = FrontendConfig.CELL_LEN
        # 棋盤線條數量 ( 幾乘幾的棋盤 )
        line_count = FrontendConfig.LINE_COUNT

        star_point_width = FrontendConfig.STAR_POINT_WIDTH
        star_point_len_4 = 4  * cell_len
        star_point_len_back_4 = (line_count - 3) * cell_len
        star_point_len_center = ((line_count + 1) / 2)  * cell_len
        star_point_list = [(star_point_len_4, star_point_len_4) ,(star_point_len_4, star_point_len_back_4),
            (star_point_len_back_4, star_point_len_4) ,(star_point_len_back_4, star_point_len_back_4),
            (star_point_len_center, star_point_len_center)]
        for i in range(len(star_point_list)):
            pygame.draw.circle(surface, black, star_point_list[i], star_point_width)
