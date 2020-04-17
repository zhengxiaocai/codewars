"""
https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

"""


def solution(s):
    return ''.join(' {}'.format(i) if i.isupper() else i for i in s)


if __name__ == '__main__':
    print(solution("helloWorld"), "hello World")
    print(solution("camelCase"), "camel Case")
    print(solution("breakCamelCase"), "break Camel Case")


