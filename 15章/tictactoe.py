# tictactoe.py, オブジェクト指向でない三目並べゲーム

ALL_SPACES = list("123456789")  # 辞書型の盤面データに対するキー
X, O, BLANK = "X", "O", " "     # プレイヤーや空き場所を表す文字定数


def get_blank_board():
    """新規の盤面を作成する."""
    board = {}  # 辞書型のデータとして盤面を表す
    for space in ALL_SPACES:
        board[space] = BLANK  # すべて空欄で初期化
    return board


def get_board_str(board):
    """盤面の状態を文字列として返す."""
    return f"""
      {board["1"]}|{board["2"]}|{board["3"]}  1 2 3
      -+-+-
      {board["4"]}|{board["5"]}|{board["6"]}  4 5 6
      -+-+-
      {board["7"]}|{board["8"]}|{board["9"]}  7 8 9"""


def is_valid_space(board, space):
    """有効な入力かつ指定箇所が空欄であれば True を返す."""
    return space in ALL_SPACES and board[space] == BLANK


def is_winner(board, player):
    """playerが勝者なら True を返す."""
    b, p = board, player  # 変数名を短くする (構文糖と呼ばれる)
    # 縦 3 箇所・横 3 箇所・斜め 2 箇所にマークが揃っているかチェック
    return (
        (b["1"] == b["2"] == b["3"] == p) or  # 横上段
        (b["4"] == b["5"] == b["6"] == p) or  # 横中段
        (b["7"] == b["8"] == b["9"] == p) or  # 横下段

        (b["1"] == b["4"] == b["7"] == p) or  # 縦左列
        (b["2"] == b["5"] == b["8"] == p) or  # 横中列
        (b["3"] == b["6"] == b["9"] == p) or  # 横右列
        
        (b["3"] == b["5"] == b["7"] == p) or  # 斜め
        (b["1"] == b["5"] == b["9"] == p)     # 斜め
    )


def  is_board_full(board):
    """盤面に空き場所がなくなったら True を返す."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # 1箇所でも空きが見つかったら False を返す
    return True  # 空きが見つからなかったので True を返す


def update_board(board, space, mark):
    """盤面の指定場所にマークする."""
    board[space] = mark


def main():
    """三目並べのゲームをはじめる."""
    print("三目並べゲームだよ！")
    game_board = get_blank_board()        # 辞書型の盤面データを生成する
    current_player, next_player = X, O  # Xが先攻、Oが後攻

    while True:
        print(get_board_str(game_board))  # 盤面を画面に表示

        # プレイヤーが 1-9 の数値を入力するまで入力を促す
        move = None
        while not is_valid_space(game_board, move):
            print(f"{current_player}の置き場所は？ (1-9)")
            move = input()

        update_board(game_board, move, current_player)  # 盤面を更新する

        # ゲームの終了判定
        if is_winner(game_board, current_player):  # まずは勝ち負け判定
            print(get_board_str(game_board))
            print(f"{current_player}の勝ち！")
            break
        elif is_board_full(game_board):  # 次に引き分け判定
            print(get_board_str(game_board))
            print("引き分け！")
            break
        
        current_player , next_player = next_player, current_player  # プレイヤー交代
    print("お疲れさまでした！")


if __name__ == "__main__":
    main()  # 実行時に main() を呼び出す (import された場合は実行しない)
