""" 四目並べ, by Al Sweigart al@inventwithpython.com
コネクトフォーに似た、タイルが4つ並ぶように落とすゲーム。"""

import sys

# 盤面表示に使う定数
EMPTY_SPACE = "."  # 数えやすいようにスペースはピリオドで表す
PLAYER_X = "X"
PLAYER_O = "O"

# 注意: BOARD_WIDTH を変更したときは BOARD_TEMPLATE と COLUMN_LABELS も変更すること
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# 盤面表示のテンプレート文字列
BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""


def get_new_board():
    """ 四目並べの盤面を表す辞書を返す。

    キーは (列のインデックス, 行のインデックス) のような2つの整数のタプルで、
    値は"X", "O", "."のいずれかになる （ピリオドは空白を表す）。 """
    board = {}

    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            board[(column_index, row_index)] = EMPTY_SPACE
    return board


def display_board(board):
    """ 盤面とタイルを出力する。 """
    # 盤面テンプレートの format() に渡すデータのリストを用意する。
    # リストに格納するデータは、左から右、上から下に向かう順番で、
    # 盤面上のタイルと空白部分の情報になっている。
    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            tile_chars.append(board[(column_index, row_index)])
    
    # 盤面を表示
    print(BOARD_TEMPLATE.format(*tile_chars))


def get_player_move(player_tile, board):
    """ プレイヤーに、どの列にタイルを落とすかを決めてもらう。
    
    タイルの落ちる場所を (行, 列) のタプルで返す。 """
    while True:  # プレイヤーから有効な入力があるまで入力を促す
        print(f"Player {player_tile}, 1から {BOARD_WIDTH} または QUIT と入力してください:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("お疲れさまでした！")
            sys.exit()
        
        if response not in COLUMN_LABELS:
            print(f"1 から {BOARD_WIDTH} までの数字を入力してください:")
            continue  # 再度入力を促す

        column_index = int(response) - 1  # 0 ベースのインデックスにするため -1 しておく

        # 列が一杯の場合は再度入力を促す
        if board[(column_index, 0)] != EMPTY_SPACE:
            print("その列は一杯です。他の列を選んでください。")
            continue  # 再度入力を促す

        # 一番下から空白部分を探す
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return (column_index, row_index)


def is_winner(playerTile, board):
    """ playerTile が1列に4枚揃っていたら True、そうでなければ False を返す。 """
    
    # 盤面全体を調べて1列に4枚揃っているかを確認する。
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            # 右方向へ4枚分調べる
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index)]
            tile3 = board[(column_index + 2, row_index)]
            tile4 = board[(column_index + 3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    
    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            # 下方向へ4枚分調べる
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index, row_index + 1)]
            tile3 = board[(column_index, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            # 右下方向へ4枚分調べる
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index + 1)]
            tile3 = board[(column_index + 2, row_index + 2)]
            tile4 = board[(column_index + 3, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            
            # 左下方向へ4枚分調べる
            tile1 = board[(column_index + 3, row_index)]
            tile2 = board[(column_index + 2, row_index + 1)]
            tile3 = board[(column_index + 1, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False


def is_full(board):
    """ 盤面に空白部分がない場合は True を返す。そうでない場合は False を返す。 """
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return False  # 空白が見つかったので False を返す
    return True  # 空白部分なし


def main():
    """ 四目並べのゲームを1回実行する """
    print(
        """ 四目並べ, by Al Sweigart al@inventwithpython.com

2人のプレーヤーが交互にタイルを7つの列のいずれかに落とし、
水平、垂直、斜めに4枚揃えた方が勝ち。"""
    )

    # ゲームの初期化
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:  # プレイヤーのターンを開始する
        # 盤面を表示し、入力を受け付ける
        display_board(game_board)
        player_move = get_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        # 勝ちか引き分けかをチェック
        if is_winner(player_turn, game_board):
            display_board(game_board)  # 最終的な盤面を表示
            print(f"Player {player_turn} の勝ち！")
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)  # 最終的な盤面を表示
            print("引き分け!")
            sys.exit()
        
        # プレイヤー交代
        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X


# プログラムを実行するとゲームがスタートする (インポートされた場合を除く)
if __name__ == "__main__":
    main()
