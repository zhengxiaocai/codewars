# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""
1、进制转化，十转十六 hex()；十六进制0x开头，怎么不要这个东西
2、格式化，长度为2，不够补零
"""


def rgb(r, g, b):
    def f(n):
        if n < 0:
            n = 0
        elif n > 255:
            n = 255
        return str(hex(n))[2:].upper()

    return '{:0>2}{:0>2}{:0>2}'.format(f(r), f(g), f(b))


def rgb_best(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


if __name__ == '__main__':
    print(rgb(0, 0, 0), "000000")
    print(rgb(1, 2, 3), "010203")
    print(rgb(255, 255, 255), "FFFFFF")
    print(rgb(254, 253, 252), "FEFDFC")
    print(rgb(-20, 275, 125), "00FF7D")

    """
    1、就近取数
    2、format
        str * n
        width
        补充0
    """