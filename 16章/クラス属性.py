class CreateCounter:
    count = 0  # これがクラス属性

    def __init__(self):
        CreateCounter.count += 1


print(f"Objects created: {CreateCounter.count}")
a = CreateCounter()
b = CreateCounter()
c = CreateCounter()
print(f"Objects created: {CreateCounter.count}")
