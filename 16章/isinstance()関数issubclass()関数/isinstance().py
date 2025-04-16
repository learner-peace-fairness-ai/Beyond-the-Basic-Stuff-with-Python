class ParentClass:
    pass


class ChildClass(ParentClass):
    pass


parent = ParentClass()  # ParentClass のオブジェクトを生成する
child = ChildClass()    # ChildClass のオブジェクトを生成する

print(isinstance(parent, ParentClass))
print(isinstance(parent, ChildClass))

print(isinstance(child, ChildClass))
print(isinstance(child, ParentClass))
