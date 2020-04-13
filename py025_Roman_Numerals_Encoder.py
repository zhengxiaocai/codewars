"""
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
转化为罗马数字
"""


def solution(n):
    roman_dict = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        20: 'XX',
        30: 'XXX',
        40: 'XL',
        50: 'L',
        60: 'LX',
        70: 'LXX',
        80: 'LXXX',
        90: 'XC',
        100: 'C',
        200: 'CC',
        300: 'CCC',
        400: 'CD',
        500: 'D',
        600: 'DC',
        700: 'DCC',
        800: 'DCCC',
        900: 'CM',
        1000: 'M',
        2000: 'MM',
        3000: 'MMM'
    }
    format_n = [10 ** (len(str(n)) - index - 1) * int(value) for index, value in enumerate(str(n))]
    return ''.join([roman_dict[i] for i in format_n if i])


def solution_best(n):
    ed = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    des = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    sot = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tys = ["", "M", "MM", "MMM", "MMMM"]
    return f'{tys[n // 1000]}{sot[n % 1000 // 100]}{des[n % 100 // 10]}{ed[n % 10]}'


if __name__ == '__main__':
    print(solution_best(1) == 'I')
    print(solution_best(4) == 'IV')
    print(solution_best(6) == 'VI')
    print(solution_best(14) == 'XIV')
    print(solution_best(21) == 'XXI')
    print(solution_best(89) == 'LXXXIX')
    print(solution_best(91) == 'XCI')
    print(solution_best(571), 'DLXXI')
    print(solution_best(984) == 'CMLXXXIV')
    print(solution_best(1000) == 'M')
    print(solution_best(1889) == 'MDCCCLXXXIX')
    print(solution_best(1989) == 'MCMLXXXIX')
