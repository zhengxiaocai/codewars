"""
https://www.codewars.com/kata/550498447451fbbd7600041c
1.判断两个序列是否相等，不只需要数据相同，顺序也需要相同。
2.怎样判断一个数字是1.0，还是1.1？？？
3.取平方根
"""


def comp(array1, array2):
    if (array1 and array2) or array1 == array2:
        return sorted([i**2 for i in array1]) == sorted(array2)
    return False


if __name__ == '__main__':
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    print(comp(a1, a2), True)

    b1 = [43, 79, 14, 94, 6, 82, 2]
    b2 = [1849, 6241, 196, 8836, 36, 6725, 4]
    print(comp(b1, b2), False)

    c1 = []
    c2 = []
    print(comp(c1, c2), True)

    print(sorted(b1))
    # print(sorted([sqrt(i) for i in b2]))

    # print([1, 2, 1] == [2, 1, 1])
    # print(sorted(a1))
    # print(sqrt(4))

    print(1.1%1)

    print(None == [])



