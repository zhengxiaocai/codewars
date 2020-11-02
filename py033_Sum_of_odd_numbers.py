# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python


def row_sum_odd_numbers(n):
    return sum(range(n ** 2 - n + 1, n ** 2 + n, 2))


if __name__ == '__main__':
    print(row_sum_odd_numbers(1), 1)
    print(row_sum_odd_numbers(2), 8)
    print(row_sum_odd_numbers(13), 2197)
    print(row_sum_odd_numbers(19), 6859)
    print(row_sum_odd_numbers(41), 68921)
