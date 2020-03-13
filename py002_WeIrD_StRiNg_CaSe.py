"""
https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python
给一句话，返回的时候，没个单词的偶数index变为大写，奇数变为小写
"""


def to_weird_case(s):
    return ' '.join([''.join([v.lower() if i % 2 else v.upper() for i, v in enumerate(word)]) for word in s.split()])


if __name__ == '__main__':
    print(to_weird_case('This') == 'ThIs')
    print(to_weird_case('is') == 'Is')
    print(to_weird_case('This is a test') == 'ThIs Is A TeSt')
    print(to_weird_case('Weird string case') == 'WeIrD StRiNg CaSe')

