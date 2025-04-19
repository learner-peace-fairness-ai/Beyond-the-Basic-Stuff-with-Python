class ClassWithRegularAttributes:
    def __init__(self, some_parameter):
        self.some_attribute = some_parameter


obj = ClassWithRegularAttributes("ある初期値")
print(obj.some_attribute)  # "ある初期値"と出力

obj.some_attribute = "別の値"
print(obj.some_attribute)  # "別の値"と出力

del obj.some_attribute  # some_attribute を削除
