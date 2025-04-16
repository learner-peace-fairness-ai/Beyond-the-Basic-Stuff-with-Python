class ExampleClassWithStaticMethod:
    @staticmethod
    def say_hello():
        print("Hello!")


# オブジェクトは生成されず、 say_hello() の前にクラス名が付いていることに注意
ExampleClassWithStaticMethod.say_hello()
