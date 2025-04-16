class ParentClass:
    def print_hello(self):
        print("Hello world!")


class ChildClass(ParentClass):
    # ChildClass は ParentClass のメソッド Print_hello() を継承している
    # だからコピー＆ペーストしなくてもOK!

    def some_new_method(self):
        print("ParentClass のオブジェクトにはこのメソッドがない")


class GrandchildClass(ChildClass):
    # GrandchildClass は ChildClass のメソッドをすべて継承している
    # ParentClass のメソッドも継承している

    def another_new_method(self):
        print("このメソッドは GrandchildClass のオブジェクトにしかない")


print("ParentClass のオブジェクトを作ってメソッドを呼び出す:")
parent = ParentClass()
parent.print_hello()

print("ChildClass のオブジェクトを作ってメソッドを呼び出す:")
child = ChildClass()
child.print_hello()
child.some_new_method()


print("GrandchildClass のオブジェクトを作ってメソッドを呼び出す:")
grandchild = GrandchildClass()
grandchild.print_hello()
grandchild.some_new_method()
grandchild.another_new_method()

print("エラーが発生する:")
parent.some_new_method()
