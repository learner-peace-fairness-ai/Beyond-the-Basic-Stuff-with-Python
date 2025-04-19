class ClassWithProperties:
    def __init__(self):
        self._some_attribute = "ある初期値"
    
    @property
    def some_attribute(self):  # これが"getter"メソッドに相当する
        return self._some_attribute
    
    @some_attribute.setter
    def some_attribute(self, value):  # これが"setter"メソッドに相当する
        self._some_attribute = value

    @some_attribute.deleter
    def some_attribute(self):  # これが"deleter"メソッドに相当する
        del self._some_attribute


obj = ClassWithProperties()
print(obj.some_attribute)  # "ある初期値"と出力

obj.some_attribute = "別の値"
print(obj.some_attribute)  # "別の値"と出力

del obj.some_attribute  # _some_attribute を削除
