# https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python


def consecutive(arr, a, b):
    return (arr.index(a) - arr.index(b)) in (1, -1)


def consecutive_best(arr, a, b):
    return abs(arr.index(a) - arr.index(b)) == 1


if __name__ == '__main__':
    print(consecutive([1, 3, 5, 7], 3, 7) is False)
    print(consecutive([1, 3, 5, 7], 3, 1) is True)
    print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4) is True)

    print(consecutive_best([1, 3, 5, 7], 3, 7), False)
    print(consecutive_best([1, 3, 5, 7], 3, 1), True)
    print(consecutive_best([1, 6, 9, -3, 4, -78, 0], -3, 4), True)
