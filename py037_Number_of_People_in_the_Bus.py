# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def number(bus_stops):
    # take = []
    # drop = []
    # for t, d in bus_stops:
    #     take.append(t)
    #     drop.append(d)
    # return sum(take) - sum(drop)

    return sum([i for i, j in bus_stops]) - sum([j for i, j in bus_stops])


def number_best(bus_stops):
    # TODO: 这个想法不错
    return sum(i[0] - i[1] for i in bus_stops)


if __name__ == '__main__':
    print(number_best([[10, 0], [3, 5], [5, 8]]), 5)
    print(number_best([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)
    print(number_best([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)
