class FrontendConfig():
    BLACK = 'black'
    # 棋盤顏色
    BOARD_COLOR = '#FFE153'

    # 遊戲介面長寬
    GUI_HIGH = 720
    GUI_WIDTH = 1280

    GUI_COLOR = '#F0F0F0'

    # 儲存格長度
    CELL_LEN = 40
    # 棋盤線條數量 ( 幾乘幾的棋盤 )
    LINE_COUNT = 15
    # 棋盤總長度
    BOARD_LEN = CELL_LEN * (LINE_COUNT + 1)

    #  四角 + 中間圓點的大小，數字越大，圓越大
    STAR_POINT_WIDTH = 5
