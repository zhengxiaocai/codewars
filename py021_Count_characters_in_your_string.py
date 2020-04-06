"""
https://www.codewars.com/kata/52efefcbcdf57161d4000091
返回string里的字母及出现的次数 的字典。
"""


def count(s):
    return {a: s.count(a) for a in s}


if __name__ == '__main__':
    print(count('aba'), {'a': 2, 'b': 1})
    print(count(''), {})

