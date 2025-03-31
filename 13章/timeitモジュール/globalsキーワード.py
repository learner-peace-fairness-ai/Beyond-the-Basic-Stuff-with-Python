import timeit

spam = 'hello'
result = timeit.timeit('print(spam)', number=1, globals=globals())
print(result)
