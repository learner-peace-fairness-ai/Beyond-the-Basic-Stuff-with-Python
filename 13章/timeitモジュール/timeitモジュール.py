import timeit

result1 = timeit.timeit('a, b = 42, 101; a = a ^ b; b = a ^ b; a = a ^ b')
print(result1)

result2 = timeit.timeit('a, b = 42, 101; temp = a; a = b; b = temp')
print(result2)

result3 = timeit.timeit('a, b = 42, 101; a, b = b, a')
print(result3)
