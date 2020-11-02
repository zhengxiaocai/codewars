# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python


def friend(x):
    return [i for i in x if len(i) == 4]


if __name__ == '__main__':
    print(friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])
