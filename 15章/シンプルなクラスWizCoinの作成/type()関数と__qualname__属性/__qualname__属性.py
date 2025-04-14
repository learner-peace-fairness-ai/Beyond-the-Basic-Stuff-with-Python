print(str(type(42)))  # 型オブジェクトを str() に渡すとわかりにくい文字列が返る

print(type(42).__qualname__)  # __qualname__ 属性を使うとわかりやすい
