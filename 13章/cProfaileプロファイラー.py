import cProfile


def add_up_numbers():
    total = 0
    for i in range(1, 1000001):
        total += i


cProfile.run('add_up_numbers()')
