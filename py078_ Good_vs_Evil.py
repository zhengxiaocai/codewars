"""
https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python

列表生成式，在一个zip里边的时候，可以简写：
[x + y for x, y in zip(a, b)]
"""


def good_vs_evil(good, evil):
    g = [1, 2, 3, 3, 4, 10]
    e = [1, 2, 2, 2, 3, 5, 10]
    g_v = sum([x * int(y) for x, y in zip(g, good.split(' '))])
    e_v = sum([x * int(y) for x, y in zip(e, evil.split(' '))])
    print(g_v, e_v)
    if g_v > e_v:
        result = 'Good triumphs over Evil'
    elif g_v < e_v:
        result = 'Evil eradicates all trace of Good'
    else:
        result = 'No victor on this battle field'
    return 'Battle Result: {}'.format(result)


if __name__ == '__main__':
    print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'), 'Battle Result: Evil eradicates all trace of Good',
          'Evil should win')
    print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil',
          'Good should win')
    print(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'), 'Battle Result: No victor on this battle field',
          'Should be a tie')
