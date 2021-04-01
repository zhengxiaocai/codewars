# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python


def zero(s=0):  # your code here
    if s:
        return eval('0 {}'.format(s))
    else:
        return 0


def one(s=0):  # your code here
    if s:
        return eval('1 {}'.format(s))
    else:
        return 1


def two(s=0):  # your code here
    if s:
        return eval('2 {}'.format(s))
    else:
        return 2


def three(s=0):  # your code here
    if s:
        return eval('3 {}'.format(s))
    else:
        return 3


def four(s=0):  # your code here
    if s:
        return eval('4 {}'.format(s))
    else:
        return 4


def five(s=0):  # your code here
    if s:
        return eval('5 {}'.format(s))
    else:
        return 5


def six(s=0):  # your code here
    if s:
        return eval('6 {}'.format(s))
    else:
        return 6


def seven(s=0):  # your code here
    if s:
        return eval('7 {}'.format(s))
    else:
        return 7


def eight(s=0):  # your code here
    if s:
        return eval('8 {}'.format(s))
    else:
        return 8


def nine(s=0):  # your code here
    if s:
        return eval('9 {}'.format(s))
    else:
        return 9


def plus(n):  # your code here
    return '+ {}'.format(n)


def minus(n):  # your code here
    return '- {}'.format(n)


def times(n):  # your code here
    return '* {}'.format(n)


def divided_by(n):  # your code here
    return '// {}'.format(n)


if __name__ == '__main__':
    print(seven(times(five())), 35)
    print(four(plus(nine())), 13)
    print(eight(minus(three())), 5)
    print(six(divided_by(two())), 3)

    # print(zero())
    # print(plus(zero()))
    # print(zero(plus(zero())))
    # print(eval('0 {}'.format('+0')))
    # print(eval('1 + 1'))
    # print(eval('0 + 0'))
