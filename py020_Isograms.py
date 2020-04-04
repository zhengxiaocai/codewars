"""
https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
string不存在重复字母就返回true。忽略大小写。
"""


def is_isogram(string):
    return all(string.lower().count(i) <= 1 for i in string)


def is_isogram_best(string):
    return len(string) == len(set(string.lower()))


if __name__ == '__main__':
    print(is_isogram_best("Dermatoglyphics"), True)
    print(is_isogram_best("isogram"), True)
    print(is_isogram_best("aba"), False)
    print(is_isogram_best("moOse"), False)
    print(is_isogram_best("isIsogram"), False)
    print(is_isogram_best(""), True)

    # print("moOse".count('O'))

