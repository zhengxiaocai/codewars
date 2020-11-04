# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python


def remove_smallest(numbers):
    numbers.remove(min(numbers, default=None))
    return numbers


if __name__ == '__main__':
    print(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])
    print(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])
    print(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1])
    print(remove_smallest([]), [])

    print(min([], default=None))
