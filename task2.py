
''' Задача 2. Дан массив целых чисел. Нужно удалить из него нули.
Можно использовать только О(1) дополнительной памяти '''


def task2_v1(lst1):
    ''' вернуть список без 0
    для памяти O(1) придётся изменить массив '''
    if not lst1:
        return lst1

    p1 = len(lst1) - 1

    while p1 >= 0:
        if lst1[p1] == 0:
            del lst1[p1]
        p1 -= 1
    return lst1


def task2_v2(lst1):
    ''' немного "жульничества" если мы хотим перебирать все элементы, но без 0
    не изменяя lst1, но соблюда O(1) по памяти '''
    for x in lst1:
        if x == 0:
            continue
        yield x


if __name__ == '__main__':
    list1 = [0, 1, 4, 7, 9, 7, 0, 0, 1, -99, 5]
    print(task2_v1(list1))
    print(list(task2_v2(list1)))

    import timeit
    import random
    N = 100000
    list1 = [random.randint(-10, 10) for _ in range(N)]
    print(timeit.timeit('task2_v1(list1)', globals=globals(), number=10))
    print(timeit.timeit('list(task2_v2(list1))', globals=globals(), number=10))
