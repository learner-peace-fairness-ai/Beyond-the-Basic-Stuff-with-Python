import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)  # 引数の整数は __init__() に渡される
print(purse)
print(f"G: {purse.galleons}, S: {purse.sickles}, K: {purse.knuts}")
print(f"Total value: {purse.value()}")
print(f"Weight: {purse.weight_in_grams()} grams")
print()

coin_jar = wizcoin.WizCoin(13, 0, 0)  # 引数の整数は __init__() に渡される
print(coin_jar)
print(f"G: {coin_jar.galleons}, S: {coin_jar.sickles}, K: {coin_jar.knuts}")
print(f"Total value: {coin_jar.value()}")
print(f"Weight: {coin_jar.weight_in_grams()} grams")
