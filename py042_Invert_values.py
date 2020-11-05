# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python


def invert(lst):
    return [-i for i in lst]


if __name__ == '__main__':
    print(invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5])
    print(invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5])
    print(invert([]) == [])
