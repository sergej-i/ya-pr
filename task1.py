''' Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке,
но нет во 2-ом. Оценить эффективность своего решения. '''

def task1_v1(lst1, lst2):
    ''' есть в списке1 и нет в списке2 '''
    if not lst2:
        return lst1

    # тут можно было бы lst1.sort(), но обычно это не то что нужно
    # O(n log n) + O(k log k), где n = len(lst1), k = len(lst2)
    lst1srt = sorted(lst1)
    lst2srt = sorted(lst2)
    rc = []
    p2 = 0  # индекс на втором листе
    x2 = lst2srt[p2]
    # O(n) + O(k), где n = len(lst1), k = len(lst2)
    for x1 in lst1srt:
        if x1 < x2:
            rc.append(x1)
        elif x1 > x2:
            while x1 > x2 and p2 < len(lst2srt) - 1:
                p2 += 1
                x2 = lst2srt[p2]
            if x1 != x2:
                rc.append(x1)
    return rc


def task1_v2(lst1, lst2):
    ''' в лоб: для теста более хитрого решения '''
    # O(n * k), где n = len(lst1), k = len(lst2)
    rc = []
    for x1 in lst1:
        if x1 not in lst2:
            rc.append(x1)
    return rc


if __name__ == '__main__':
    list1 = [0, 1, 4, 7, 9, 7, -99, 5]
    list2 = [1, 9, -1, -7, 7, 99]
    print(task1_v1(list1, list2))
    print(task1_v2(list1, list2))

    import timeit
    import random
    N = 100000
    list1 = [random.randint(-10000, 10000) for _ in range(N)]
    list2 = [random.randint(-10000, 9000) for _ in range(N)]
    print(timeit.timeit('task1_v1(list1, list2)', globals=globals(), number=10))
    print(timeit.timeit('task1_v2(list1, list2)', globals=globals(), number=1))

    # v1 -> 1.3091706020059064
    # v2 -> 39.81458305797423
