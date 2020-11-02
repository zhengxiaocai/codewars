# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python


def open_or_senior(data):
    return ['Senior' if i >= 55 and j > 7 else 'Open' for i, j in data]


if __name__ == '__main__':
    print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]), ['Open', 'Senior', 'Open', 'Senior'])
    print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]), ['Open', 'Open', 'Senior', 'Open'])
