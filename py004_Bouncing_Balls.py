"""
https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

"""


def bouncingBall(h, bounce, window):
    if 0 < window < h and 0 < bounce < 1:
        times = 0
        while h > window:
            times += 2
            h *= bounce
        return times - 1
    else:
        return -1


if __name__ == '__main__':
    print(bouncingBall(3, 0.66, 1.5), 3)
    print(bouncingBall(30, 0.66, 1.5), 15)
    print(bouncingBall(2, 0.5, 1), 1)
    print(bouncingBall(30, 0.75, 1.5), 21)
    print(bouncingBall(30, 0.4, 10), 3)
    print(bouncingBall(40, 1, 10), -1)
    print(bouncingBall(-5, 0.66, 1.5), -1)

