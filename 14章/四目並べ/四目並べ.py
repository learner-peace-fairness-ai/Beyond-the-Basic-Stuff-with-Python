"""タイルが4つ並ぶように落とすゲーム.

ルール:
    ・ボードは 6行 * 7列 の直立型
    ・プレイヤーは"O"と"X"の2人
    ・プレイヤーは交互にある列に1つのタイルを落とす
    ・空白のマスは"."
    ・自分のタイルを縦、横、斜めに4つ並べたらクリア
    ・ボードがいっぱいになったら引き分け"""

import sys

BOARD_HEIGHT = 6
BOARD_WIDTH = 7
EMPTY_MARK = '.'


def create_new_board():
    board = []
    for ri in range(BOARD_HEIGHT):
        row = [EMPTY_MARK] * BOARD_WIDTH
        board.append(row)
    return board


def display_board(board):
    # ヘッダ行
    for column_name in range(1, BOARD_WIDTH + 1):
        print(column_name, end="")
    print()

    # ボード
    for ri in range(BOARD_HEIGHT):
        for ci in range(BOARD_WIDTH):
            print(board[ri][ci], end="")
        print()


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_valid_input(command):
    if not is_integer(command):
        return False
    
    num = int(command)
    return 1 <= num <= BOARD_WIDTH


def is_full_of_tiles_in_column(command, board):
    ci = int(command) - 1  # boardのインデックスに合わせる
    first_row = board[0]
    return first_row[ci] != EMPTY_MARK


def drop_tile(command, board, tile):
    ci = int(command) - 1  # boardのインデックスに合わせる

    # 上からタイルを置けるマスを探す
    ri_empty = -1
    for ri in range(BOARD_HEIGHT):
        if board[ri][ci] != EMPTY_MARK:
            break
        ri_empty = ri
    
    board[ri_empty][ci] = tile


def is_four_tiles_vertically(board):
    for ci in range(BOARD_WIDTH):
        for ri in range(BOARD_HEIGHT - 3):
            if board[ri][ci] == EMPTY_MARK:
                continue
            
            tile1 = board[ri][ci]
            tile2 = board[ri + 1][ci]
            tile3 = board[ri + 2][ci]
            tile4 = board[ri + 3][ci]
            if tile1 == tile2 == tile3 == tile4:
                return True
    return False


def is_four_tiles_horizontally(board):
    for ri in range(BOARD_HEIGHT):
        for ci in range(BOARD_WIDTH - 3):
            if board[ri][ci] == EMPTY_MARK:
                continue
            
            tile1 = board[ri][ci]
            tile2 = board[ri][ci + 1]
            tile3 = board[ri][ci + 2]
            tile4 = board[ri][ci + 3]
            if tile1 == tile2 == tile3 == tile4:
                return True
    return False


def is_four_tiles_diagonally(board):
    # 右斜めに4つ並んでいるか
    for ri in range(BOARD_HEIGHT - 3):
        for ci in range(BOARD_WIDTH - 3):
            if board[ri][ci] == EMPTY_MARK:
                continue
            
            tile1 = board[ri][ci]
            tile2 = board[ri + 1][ci + 1]
            tile3 = board[ri + 2][ci + 2]
            tile4 = board[ri + 3][ci + 3]
            if tile1 == tile2 == tile3 == tile4:
                return True
    
    # 左斜めに4つ並んでいるか
    for ri in range(BOARD_HEIGHT - 3):
        for ci in range(BOARD_WIDTH - 3):
            if board[ri][ci + 3] == EMPTY_MARK:
                continue
            
            tile1 = board[ri][ci + 3]
            tile2 = board[ri + 1][ci + 2]
            tile3 = board[ri + 2][ci + 1]
            tile4 = board[ri + 3][ci]
            if tile1 == tile2 == tile3 == tile4:
                return True
    
    return False


def is_clear(board):
    # 縦に4つ並んでいるか
    if is_four_tiles_vertically(board):
        return True
    # 横に4つ並んでいるか
    elif is_four_tiles_horizontally(board):
        return True
    # 斜めに4つ並んでいるか
    elif is_four_tiles_diagonally(board):
        return True
    else:
        return False


PLAYER_O = "o"
PLAYER_X = "x"
MAX_NUMBER_OF_TURNS = BOARD_HEIGHT * BOARD_WIDTH

board = create_new_board()
player = PLAYER_O
for i in range(MAX_NUMBER_OF_TURNS):
    display_board(board)

    # タイルを落とす列を決定
    print(" 1 から 7 のどの列にタイルを落とすかを入力してください。（終了する場合は QUIT）")
    print("\tex) 1")
    command = input(f"Player {player}: ").upper().strip()
    if command == "QUIT":
        print("プログラムを終了します。")
        sys.exit()

    # 入力が正しいかチェック
    if not is_valid_input(command):
        print("無効な入力です。")
        continue

    # 列にタイルを置けるかチェック
    if is_full_of_tiles_in_column(command, board):
        print(f"列 {command} にはタイルを置けません。")
        continue

    # ボードにタイルを入力
    drop_tile(command, board, player)

    # クリアしたかチェック
    if is_clear(board):
        print(f"{player} の勝ちです。")
        display_board(board)
        sys.exit()

    # プレイヤー交代
    if player == PLAYER_O:
        player = PLAYER_X
    elif player == PLAYER_X:
        player = PLAYER_O

print("引き分けです。")
display_board(board)
