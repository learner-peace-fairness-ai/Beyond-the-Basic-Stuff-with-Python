class ParentClass:
    pass


class ChildClass(ParentClass):
    pass


print(issubclass(ChildClass, ParentClass))  # ChildClass は ParentClass の子クラス
print(issubclass(ChildClass, ChildClass))   # ChildClass は ChildClass の子クラス

print(issubclass(ChildClass, str))          # ChildClass は str の子クラスではない
