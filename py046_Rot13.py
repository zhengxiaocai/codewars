# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
import string


def rot13(message):
    def my_encode(i):
        if str(i).islower():
            return string.ascii_lowercase[string.ascii_lowercase.index(i) - 13]
        else:
            return string.ascii_uppercase[string.ascii_uppercase.index(i) - 13]

    return ''.join([my_encode(i) if i.isalpha() else i for i in message])


if __name__ == '__main__':
    print(rot13("test"), "grfg")
    print(rot13("Test"), "Grfg")
    # print(string.ascii_lowercase[string.ascii_lowercase.index('e') - 13])
    print(string.ascii_letters)

    print(range(1, 5))
