# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python


def nb_year(p0, percent, aug, p):
    y = 0
    while p0 < p:
        p0 = p0 * (1 + percent / 100) + aug
        y += 1
    return y


if __name__ == '__main__':
    print(nb_year(1500, 5, 100, 5000), 15)
    print(nb_year(1500000, 2.5, 10000, 2000000), 10)
    print(nb_year(1500000, 0.25, 1000, 2000000), 94)
