class ExampleClass:
    def example_regular_method(self):
        print("これは通常のメソッド。")
    
    @classmethod
    def example_class_method(cls):
        print("これはクラスメソッド。")


# オブジェクトを生成せずにクラスメソッドを呼ぶ
ExampleClass.example_class_method()

obj = ExampleClass()
# 次の2行は等価
obj.example_class_method()
obj.__class__.example_class_method()
