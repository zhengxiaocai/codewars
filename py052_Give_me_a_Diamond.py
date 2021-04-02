# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python

def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    n = n // 2 + 1
    temp = []
    for i in range(1, n + 1):
        temp.append((n - i) * ' ' + (i * 2 - 1) * '*' + '\n')
    return ''.join(temp + temp[:n-1][::-1])


if __name__ == '__main__':
    expected = " *\n"
    expected += "***\n"
    expected += " *\n"
    print(diamond(1) == "*\n")
    print(diamond(2) is None)
    print(diamond(3) == expected)
    print(diamond(5) == "  *\n ***\n*****\n ***\n  *\n")
    # print(diamond(5))
    print(diamond(0) is None)
    print(diamond(-3) is None)
