"""
https://www.codewars.com/kata/543e8390386034b63b001f31/train/python
编写一个方法，该方法将字符串作为参数，并将每个字符出现在字符串中的时间分组为哈希，
并按出现次数最高的顺序进行排序。
字符应按字母顺序排序，例如：
get_char_count("cba") == {1: ["a", "b", "c"]}
您应该忽略空格，特殊字符，并将大写字母视为小写字母。
"""


from collections import defaultdict


def get_char_count(s):
    result = defaultdict(list)
    for i in s.lower():
        if i.isdigit() or i.isalpha():
            result[s.lower().count(i)].append(i)
    result = {key: sorted(list(set(value))) for key, value in result.items()}
    return dict(sorted(result.items(), reverse=True))


if __name__ == '__main__':
    print(get_char_count("Mississippi") == {4: ["i", "s"], 2: ["p"], 1: ["m"]})
    print(get_char_count("Hello. Hello? HELLO!") == {6: ["l"], 3: ["e", "h", "o"]})
    print(get_char_count("aaa...bb...c!") == {3: ["a"], 2: ["b"], 1: ["c"]})
    print(get_char_count("abc123") == {1: ["1", "2", "3", "a", "b", "c"]})
    print(get_char_count("aaabbbccc") == {3: ["a", "b", "c"]})


