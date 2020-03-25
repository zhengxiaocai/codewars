"""
https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

"""
from math import pow


def find_n(m):
    def f(n):
        result = []
        a = 0
        for i in range(n):
            a += i ** 3
            yield a
        # return result
    v = int(pow(m, 1/3))
    b = f(v)
    print(list(b))
    # 为什么这里分明已经在判断已经进去了，但是后边index()却说不在list？
    # 或者有啥办法可以取到生成器的下标？
    if m in b:
        return list(b).index(m)
    else:
        return -1


def find_nb(m):
    sum = 0
    for i in range(int(pow(m, 1/3))):
        sum += i ** 3
        if m == sum:
            return i
        elif sum > m:
            break
    return -1


# def find_nb(m):



if __name__ == '__main__':
    print(find_nb(4183059834009), 2022)
    print(find_nb(24723578342962), -1)
    print(find_nb(135440716410000), 4824)
    print(find_nb(40539911473216), 3568)
    print(find_nb(26825883955641), 3218)

    # print(pow(40539911473216, 1/3))
    # print(3.0 / 1)

    # print(4183059834009 in [4183059834009, 1])




