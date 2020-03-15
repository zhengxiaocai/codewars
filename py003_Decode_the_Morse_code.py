"""
https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python
翻译摩斯密码，每个单词之间用3个空格分开，每个字母之间用1个空格分开。
有个全局变量字典：MORSE_CODE，可以转换摩斯密码。
"""


def decodeMorse(morse_code):
    return ' '.join([''.join([MORSE_CODE[cha] for cha in word.split(' ')]) for word in morse_code.strip().split('   ')])


if __name__ == '__main__':
    MORSE_CODE = {'....': 'H', '.': 'E', '-.--': 'Y', '.---': 'J',
                  '..-': 'U', '-..': 'D'}
    print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
    print(decodeMorse('.... . -.--'), 'HEY')
    print(decodeMorse('....'), 'H')
    # print(decodeMorse(''), '')
    print(decodeMorse(' . '), 'E')


