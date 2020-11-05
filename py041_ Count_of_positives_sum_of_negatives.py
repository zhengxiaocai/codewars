# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python


def count_positives_sum_negatives(arr):
    if arr:
        return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])]
    return arr


if __name__ == '__main__':
    print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65])
    print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50])
    print(count_positives_sum_negatives([1]) == [1, 0])
    print(count_positives_sum_negatives([-1]) == [0, -1])
    print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0])
    print(count_positives_sum_negatives([]) == [])
