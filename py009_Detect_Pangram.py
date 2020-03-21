"""
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
判断一个字符串，是否26个英文字母至少出现一次字母A-Z（大小写无关）
"""


def is_pangram(s):
    return len(set([i.lower() for i in s if i.isalpha()])) == 26


if __name__ == '__main__':
    pangram = "The quick, brown fox jumps over the lazy dog!"
    print(is_pangram(pangram), True)
