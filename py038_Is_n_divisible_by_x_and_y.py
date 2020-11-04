# https://www.codewars.com/kata/5545f109004975ea66000086/train/python


def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


if __name__ == '__main__':
    print(is_divisible(3, 3, 4), False)
    print(is_divisible(12, 3, 4), True)
    print(is_divisible(8, 3, 4), False)
    print(is_divisible(48, 3, 4), True)
