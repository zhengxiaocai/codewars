# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda a: (sum(int(i) for i in a), a)))


if __name__ == '__main__':
    print(order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99")
    print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") ==
          "11 11 2000 10003 22 123 1234000 44444444 9999")
