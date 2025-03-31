import timeit

result = timeit.timeit('random.randint(1, 100)', setup='import random', number=10000000)
print(result)
