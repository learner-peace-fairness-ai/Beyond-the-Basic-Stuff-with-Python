""" ハノイの塔, by Al Sweigart al@inventwithpython.com
積み上げ型パズルゲーム """

import copy
import sys

TOTAL_DISKS = 5  # 円盤数を増やすと難度アップ

# 最初はすべての円盤がAの塔にある
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """ ハノイの塔のゲームを1回実行する """
    print(
        """ ハノイの塔, by Al Sweigart al@inventwithpython.com

円盤を1枚ずつ別の塔に移動させます。大きな円盤を小さな円盤の上に乗せることはできません。

詳細は https://ja.wikipedia.org/wiki/ハノイの塔
"""
    )

    """ towers はキー "A", "B", "C" と塔を表す円盤のリストからなる辞書型データ。
    リストには円盤のサイズを表す整数値が含まれる。円盤が5枚の場合、
    リスト [5, 4, 3, 2, 1] は完成した塔を表す。空白のリスト [] は円盤のない塔を表す。
    リスト [1, 3] は、大きい円盤が小さい円盤の上に乗っていることになり無効である。
    リスト [3, 1] は、小さい円盤が大きい円盤の上に乗せられるので有効である。"""
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:  # 1回のループで1ターン
        # 塔と円盤を表示する
        dispaly_towers(towers)
        
        # プレイヤーに入力を求める
        from_tower, to_tower = get_player_move(towers)

        # 円盤を from_tower から to_tower に移動する
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        # ゲームをクリアできているかをチェック
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            dispaly_towers(towers)  # 最後の状態を出力
            print(" クリアしました！おめでとうございます！ ")


def get_player_move(towers):
    """ プレイヤーに入力を求める。

       (from_tower: 移動元の塔, to_tower: 移動先の塔) の形で返す。 """
    while True:  # プレイヤーから有効な入力があるまで入力を促す
        print(' どの塔からどの塔に動かすかを文字で入力してください。終了する場合は "QUIT" と入力してください。')
        print(' (例: AからBに移動する場合は "AB" と入力)')
        print()
        response = input("> ").upper().strip()
        if response == "QUIT":
            print(" お疲れさまでした！ ")
            sys.exit()
        
        # 入力が有効な文字かどうかを確認する
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("AB, AC, BA, BC, CA, CB のいずれかを入力してください。 ")
            continue  # 再度入力を促す

        # わかりやすい変数名にしておく
        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            # 移動元の塔に円盤が1つもないのはダメ
            print(" その塔に円盤がありません。 ")
            continue  # 再度入力を促す
        elif len(towers[to_tower]) == 0:
            # 移動先の塔が空ならどんな円盤でも OK
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print(" 小さい円盤の上に大きい円盤を置くことはできません。 ")
            continue  # 再度入力を促す
        else:
            # 有効な入力なので、選ばれた塔のセットを返す
            return from_tower, to_tower


def dispaly_towers(towers):
    """ 塔と円盤を出力する """

    # 塔を3つ出力する
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)  # ポールだけを出力
            else:
                display_disk(tower[level])  # 円盤を出力
        print()
    
    # 塔のラベル A, B, C を出力する
    empty_space = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))


def display_disk(width):
    """ 大きさが width の円盤を出力する。 width が 0 の場合は円盤なし。 """
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        # 円盤がないポール部分の出力
        print(f"{empty_space}||{empty_space}", end="")
    else:
        # 円盤を出力
        disk = "@" * width

        num_label = f'{width:_>2}'
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")


# プログラムを実行するとゲームがスタートする (インポートされた場合を除く)
if __name__ == "__main__":
    main()
