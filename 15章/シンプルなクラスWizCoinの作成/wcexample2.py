import wizcoin

change = wizcoin.WizCoin(9, 7 , 20)
print(change.sickles)  # 7 を出力

change.sickles +=10
print(change.sickles)  # 17 を出力

pile = wizcoin.WizCoin(2, 3, 31)
print(pile.sickles)

pile.some_new_attribute = "a new attr"  # 新たな属性を作成
print(pile.some_new_attribute)
