"""
https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python

"""
import re


def valid_phone_number(phone):
    s = r'^\(\d{3}\) \d{3}\-\d{4}$'
    return re.match(s, phone) != None


def valid_phone_number_best(phone):
    s = r'^\(\d{3}\) \d{3}\-\d{4}$'
    return bool(re.match(s, phone))


if __name__ == '__main__':
    print(valid_phone_number_best("(123) 456-7890"), True)
    print(valid_phone_number_best("(123) 456-7890"), True)
    print(valid_phone_number_best("(1111)555 2345"), False)
    print(valid_phone_number_best("(098) 123 4567"), False)
    print(valid_phone_number_best("abc(123) 456-7890"), False)


