# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize(n):
    return list(reversed([int(i) for i in str(n)]))


def digitize_best(n):
    return list(map(int, str(n)[::-1]))


if __name__ == '__main__':
    print(digitize_best(35231), [1, 3, 2, 5, 3])
    print(digitize_best(348597), [7, 9, 5, 8, 4, 3])
