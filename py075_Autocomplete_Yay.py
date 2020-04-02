"""
https://www.codewars.com/kata/5389864ec72ce03383000484

自动完成功能将接收输入字符串和字典数组，并从字典中返回以输入字符串开头的值。
如果匹配项超过5个，则将输出限制为前5个结果。如果没有匹配项，则返回一个空数组。

1.判断一个字符是否是字母：
str.isalpha()
2.判断一个字符是否是数字，只能判断是整型：
str.isdigit()
3.判断一个字符串
"""


def autocomplete(input_, d):
    input_ = ''.join([i for i in input_ if i.isalpha()])
    return [i for i in d if i.lower().startswith(input_.lower())][:5]


if __name__ == '__main__':
    dictionary = ['abnormal',
                  'arm-wrestling',
                  'absolute',
                  'airplane',
                  'airport',
                  'amazing',
                  'apple',
                  'ball']

    print(autocomplete('ai', dictionary) == ['airplane', 'airport'])
    print(autocomplete('a', dictionary) == ['abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport'])

    print('123.1'.isdigit())
    'a'.isspace()

