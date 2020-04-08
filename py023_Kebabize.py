"""
https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python
将驼峰案例字符串转换为烤肉串案例
    返回的字符串应仅包含小写字母
"""


def kebabize(string):
    return ''.join(['-{}'.format(j.lower()) if j.isupper() else j for j in ''.join([i for i in string if i.isalpha()])]).strip('-')


if __name__ == '__main__':
    print(kebabize('camelsHaveThreeHumps') == 'camels-have-three-humps')
    print(kebabize('camelsHave3Humps') == 'camels-have-humps')
    print(kebabize('myCamelCasedString') == 'my-camel-cased-string')
    print(kebabize('myCamelHas3Humps') == 'my-camel-has-humps')
    print(kebabize('SOS') == 's-o-s')
    print(kebabize('42') == '')
    print(kebabize('CodeWars') == 'code-wars')



