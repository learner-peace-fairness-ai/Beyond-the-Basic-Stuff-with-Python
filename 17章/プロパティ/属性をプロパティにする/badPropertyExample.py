class ClassWithBadProperty:
    def __init__(self):
        self.some_attribute = "ある初期値"
    
    @property
    def some_attribute(self):  # これが"getter"メソッドに相当する
        # "self._some_attribute"のアンダースコア(_)をつけ忘れたため
        # プロパティを使うことになり、再度 getter メソッドが呼ばれることになる
        return self.some_attribute
    
    @some_attribute.setter
    def some_attribute(self, value):  # これが"setter"メソッドに相当する
        self._some_attribute = value


obj = ClassWithBadProperty()
print(obj.some_attribute)  # getter がさらに getter を呼び出すのでエラー
