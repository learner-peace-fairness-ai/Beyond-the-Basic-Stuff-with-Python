from wizcoin import WizCoin

purse = WizCoin(2, 5, 10)
print(repr(purse))  # 内部で WizCoin の __repr__() が呼ばれる

print(str(purse))  # 内部で WizCoin の __str__() が呼ばれる

print(f"My purse contains {purse}")  # WizCoin の __str__() が呼ばれる
