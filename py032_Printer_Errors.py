# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    return f'{len([i for i in s if ord(i) - ord("m") > 0])}/{len(s)}'


def printer_error_good(s):
    return f'{len([i for i in s if i > "m"])}/{len(s)}'


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    print(printer_error_good(s), "3/56")

    """
    字符串也可以自己比较
    """
