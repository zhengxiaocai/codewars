# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def number(bus_stops):
    # take = []
    # drop = []
    # for t, d in bus_stops:
    #     take.append(t)
    #     drop.append(d)
    # return sum(take) - sum(drop)

    return sum([i for i, j in bus_stops]) - sum([j for i, j in bus_stops])


if __name__ == '__main__':
    print(number([[10, 0], [3, 5], [5, 8]]), 5)
    print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)
    print(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)