# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python


def max_sequence(arr):
    tmp = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                tmp.append(sum(arr[i: j + 1]))
    return 0 if not arr or all(i < 0 for i in arr) else max(tmp)


if __name__ == '__main__':
    print(max_sequence([]), 0)
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    print(max_sequence([-1, -2]), 0)
