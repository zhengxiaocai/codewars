def litres(time):
    return int(time / 2)


def litres_best(time):
    return time // 2


if __name__ == '__main__':
    print(litres(2), 1)
    print(litres(1.4), 0)
    print(litres(12.3), 6)
    print(litres(0.82), 0)
    print(litres(11.8), 5)
    print(litres(1787), 893)
    print(litres(0), 0)
