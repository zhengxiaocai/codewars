# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    return cc if len(cc) <= 4 else '#' * (len(cc) - 4) + cc[-4:]


def maskify_best(cc):
    return "#" * (len(cc) - 4) + cc[-4:]


if __name__ == '__main__':
    print(maskify_best(''), '')
    print(maskify_best('123'), '123')
    print(maskify_best('SF$SDfgsd2eA'), '########d2eA')

    """
    以下这两种情况，都不会报错：
    print('#' * 1)
    print('123'[-4:])
    """
