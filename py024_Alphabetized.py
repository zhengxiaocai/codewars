"""
https://www.codewars.com/kata/5970df092ef474680a0000c9/train/python

"""
from operator import itemgetter


def alphabetized(s):
    return ''.join(sorted([i for i in s if i.isalpha()], key=lambda x: x.lower()))


def alphabetized_best(s):
    return ''.join(sorted([i for i in s if i.isalpha()], key=str.lower))


if __name__ == '__main__':
    print(alphabetized("") == "")
    print(alphabetized(" ") == "")
    print(alphabetized(" a") == "a")
    print(alphabetized("a ") == "a")
    print(alphabetized(" a ") == "a")
    print(alphabetized("A b B a") == "AabB")
    print(alphabetized(
        " a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z") ==
                       "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ")
    print(alphabetized("!@$%^&*()_+=-`,") == "")
    print(alphabetized("The Holy Bible") == "BbeehHilloTy")
    print(alphabetized_best("CodeWars can't Load Today") == "aaaaCcdddeLnooorstTWy")


