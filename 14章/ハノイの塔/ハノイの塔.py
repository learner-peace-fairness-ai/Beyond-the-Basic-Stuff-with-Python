"""A塔にある完成した塔を他の塔に移す.

ルール:
    ・プレイヤーは1度に1枚の円盤を動かす
    ・一番上にある円盤を移動する
    ・小さい円盤を大きい円盤の上に置く
    ・塔はA,B,Cの3つ"""

import sys

NUM_DISKS = 3  # 円盤の数
COMPLETED_TOWER = [i for i in range(NUM_DISKS, 0, -1)]  # 末尾が最上段の円盤

towers = {"A": COMPLETED_TOWER.copy(), "B": [], "C": []}


def display_towers():
    SPACE = " "

    # 塔の最上段から順に表示
    for i in range(NUM_DISKS - 1, -1, -1):
        for name in ["A", "B", "C"]:
            tower = towers[name]

            if len(tower) >= i + 1:  # i + 1 のMAXは　NUM_DISKS
                # 円盤を表示
                print(f"{SPACE}{tower[i]}", end="")
            else:
                # 空白で埋める
                print(f"{SPACE}{SPACE}", end="")
        print()
    # 塔の名前を表示
    print(f" A B C")


def is_valid_input(command):
    return command in ("AB", "AC", "BA", "BC", "CA", "CB")


def exists_disks(tower):
    if tower:
        return True
    else:
        return False


def can_move_disk(src_tower, dst_tower):
    # 移動先に円盤がなければ無条件で置ける
    if not exists_disks(dst_tower):
        return True

    # 移動元の円盤の大きさが移動先より小さいか
    src_disk = src_tower[-1]
    dst_disk = dst_tower[-1]
    return src_disk < dst_disk


def move_disk(src_tower, dst_tower):
    dst_tower.append(src_tower.pop())


def is_clear():
    return towers["B"] == COMPLETED_TOWER or towers["C"] == COMPLETED_TOWER


while True:
    display_towers()

    # 動かす円盤を決定
    print("どの塔からどの塔に動かすかを入力してください。（終了する場合は QUIT）")
    command = input("ex) AB: ").upper().strip()
    if command == "QUIT":
        print("プログラムを終了します。")
        sys.exit()

    if not is_valid_input(command):
        print("無効な入力です。")
        continue

    src = command[0]
    dst = command[1]
    src_tower = towers[src]
    dst_tower = towers[dst]

    if not exists_disks(src_tower):
        print(f"{src}に円盤がありません。")
        continue

    if not can_move_disk(src_tower, dst_tower):
        src_disk = src_tower[-1]
        dst_disk = dst_tower[-1]
        print(
            f"{src}の円盤{src_disk}が{dst}の円盤{dst_disk}より大きいので移動できません。"
        )
        continue

    move_disk(src_tower, dst_tower)

    if is_clear():
        print("クリアしました。")
        display_towers()
        break
