"""
https://www.codewars.com/kata/5432fd1c913a65b28f000342/train/python

"""


def multiplication_table(row, col):
    c = []
    for i in range(1, row + 1):
        r = []
        for j in range(1, col + 1):
            r.append(i * j)
        c.append(r)
    return c


def multiplication_table_best(row, col):
    return [[(i+1) * (j+1) for i in range(row)] for j in range(col)]


if __name__ == '__main__':
    print(multiplication_table(2, 2) == [[1, 2], [2, 4]])
    print(multiplication_table(3, 3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]])

    print(multiplication_table_best(2, 2) == [[1, 2], [2, 4]])
    print(multiplication_table_best(3, 3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]])

