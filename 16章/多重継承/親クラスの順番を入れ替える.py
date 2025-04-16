# tictactoe_oop.py, オブジェクト指向バージョンの三目並べゲーム

ALL_SPACES = list("123456789")  # 辞書型の盤面データに対するキー
X, O, BLANK = "X", "O", " "     # プレイヤーや空き場所を表す文字定数

class TTTBoard:
    def __init__(self, use_pretty_booard=False, use_logging=False):
        """新規の盤面を作成する."""
        self._spaces = {}  # 辞書型のデータとして盤面を表す
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # すべて空欄で初期化

    def get_board_str(self):
        """盤面の状態を文字列として返す."""
        return f"""
      {self._spaces["1"]}|{self._spaces["2"]}|{self._spaces["3"]}  1 2 3
      -+-+-+
      {self._spaces["4"]}|{self._spaces["5"]}|{self._spaces["6"]}  4 5 6
      -+-+-+
      {self._spaces["7"]}|{self._spaces["8"]}|{self._spaces["9"]}  7 8 9"""
    
    def is_valid_space(self, space):
        """有効な入力かつ指定箇所が空欄であれば True を返す."""
        return space in ALL_SPACES and self._spaces[space] == BLANK
    
    def is_winner(self, player):
        """playerが勝者なら True を返す."""
        s, p = self._spaces, player  # 変数名を短くする (構文糖と呼ばれる)
        # 縦 3 箇所・横 3 箇所・斜め 2 箇所にマークが揃っているかチェック
        return (
            (s["1"] == s["2"] == s["3"] == p) or  # 横上段
            (s["4"] == s["5"] == s["6"] == p) or  # 横中段
            (s["7"] == s["8"] == s["9"] == p) or  # 横下段

            (s["1"] == s["4"] == s["7"] == p) or  # 縦左列
            (s["2"] == s["5"] == s["8"] == p) or  # 横中列
            (s["3"] == s["6"] == s["9"] == p) or  # 横右列
            
            (s["3"] == s["5"] == s["7"] == p) or  # 斜め
            (s["1"] == s["5"] == s["9"] == p)     # 斜め
        )

    def is_board_full(self):
        """盤面に空き場所がなくなったら True を返す."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # 1箇所でも空きが見つかったら False を返す
        return True  # 空きが見つからなかったので True を返す
    
    def update_board(self, space, player):
        """盤面の指定場所にマークする."""
        self._spaces[space] = player


class HintBoard(TTTBoard):
    def get_board_str(self):
        """ヒント付きの盤面を文字列として返す."""
        # TTTBoard クラスの get_board_str() を呼び出す
        board_str = super().get_board_str()

        x_can_win = False
        o_can_win = False
        original_spaces = self._spaces  # _spaces のバックアップ
        for space in ALL_SPACES:  # すべての箇所を走査
            # ここに X を置いた場合 :
            self._spaces = original_spaces.copy()
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.is_winner(X):
                x_can_win = True
            
            # ここに O を置いた場合
            self._spaces = original_spaces.copy()
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.is_winner(O):
                o_can_win = True
            
            if x_can_win and o_can_win:
                break
        
        if x_can_win:
            board_str += f"\n{X}はあと一手で勝てるよ"
        if o_can_win:
            board_str += f"\n{O}はあと一手で勝てるよ"
        
        self._spaces = original_spaces
        return board_str


class MiniBoard(TTTBoard):
    def get_board_str(self):
        """盤面の状態を縮小版の文字列として返す."""
        # BLANC を "." に変換する
        small_board = {k: v if v != BLANK else "." for k, v in self._spaces.items()}

        return f"""
          {small_board["1"]}{small_board["2"]}{small_board["3"]}  123
          {small_board["4"]}{small_board["5"]}{small_board["6"]}  456
          {small_board["7"]}{small_board["8"]}{small_board["9"]}  789"""


class HybridBoard(MiniBoard, HintBoard):
    pass


def main():
    """三目並べのゲームをはじめる."""
    print("三目並べゲームだよ！")
    game_board = HybridBoard()  # 盤面オブジェクトを生成する
    current_player, next_player = X, O  # Xが先攻、Oが後攻

    while True:
        print(game_board.get_board_str())  # 盤面を画面に表示

        # プレイヤーが 1-9 の数値を入力するまで入力を促す
        move = None
        while not game_board.is_valid_space(move):
            print(f"{current_player}の置き場所は？ (1-9)")
            move = input()
        
        game_board.update_board(move, current_player)  # 盤面を更新する
        
        # ゲームの終了判定
        if game_board.is_winner(current_player):  # まずは勝ち負け判定
            print(game_board.get_board_str())
            print(f"{current_player}の勝ち！")
            break
        elif game_board.is_board_full():  # 次に引き分け判定
            print(game_board.get_board_str())
            print("引き分け!")
            break
        
        current_player, next_player = next_player, current_player  # プレイヤー交代
    print("お疲れさまでした！")


if __name__ == "__main__":
    main()  # 実行時に main() を呼び出す (import された場合は実行しない)