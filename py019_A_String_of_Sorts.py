"""
https://www.codewars.com/kata/536c6b8749aa8b3c2600029a/train/python
定义一个接受2个字符串作为参数的方法。该方法返回按第二个字符串排序的第一个字符串。
    sort_string("foos", "of")       == "oofs"
    sort_string("string", "gnirts") == "gnirts"
    sort_string("banana", "abn")    == "aaabnn"
详细地说，第二个字符串定义了顺序。在第二个字符串中有可能重复字符，因此您应该删除重复的字符，仅保留第一个出现的字符。
第一个字符串中未出现在第二个字符串中的任何字符应按原始顺序排序到结果的末尾。

str.replace(old, new, count=-1)
count=-1代表全替换
"""


def sort_string(s, ordering):
    result = ''
    for o in ordering:
        result += o * s.count(o)
        s = s.replace(o, '')
    return result + s


if __name__ == '__main__':
    print(sort_string("foos", "of"), "oofs")
    print(sort_string("string", "gnirts"), "gnirts")
    print(sort_string("banana", "a"), "aaabnn")

    print('fooo'.replace('o', ''))
    # 还可以规定替换的次数，不规定就是全替换
    print('oaobo'.replace('o', '', 1))

