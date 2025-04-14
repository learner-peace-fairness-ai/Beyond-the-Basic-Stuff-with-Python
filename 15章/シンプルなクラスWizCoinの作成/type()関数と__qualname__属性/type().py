from pathlib import Path
import sys

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import wizcoin

print(type(42))  # 42 は int型
print(int)  # int は整数データ型の型オブジェクト
print(type(42) == int)  # 整数に対する 42 の型チェック

print(type("Hello") == int)  # 整数に対する "Hello" の型チェック

print(type(42) == wizcoin.WizCoin(2, 5, 10))  # 整数に対する WizCoin型 の型チェック

purse = wizcoin.WizCoin(2, 5, 10)
print(type(purse) == wizcoin.WizCoin)  # purse に対する WizCoin型 の型チェック
