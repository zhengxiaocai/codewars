"""
https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
如果是质数，返回True；否则返回False
但是现在代码，性能有问题。
****只需遍历至range(2, math.sqrt(n) + 1)即可。记住。
****all()
"""
import time
import math


def is_prime(num):
    if num >= 2:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    else:
        return False
    return True


def is_prime_best(n):
    return n > 1 and all(n % d for d in range(2, int(math.sqrt(n)) + 1))


if __name__ == '__main__':
    start = time.time()
    print(is_prime(0), False)
    print(is_prime(1), False)
    print(is_prime(4), False)
    print(is_prime(2), True)
    print(is_prime(73), True)
    print(is_prime(75), False)
    print(is_prime(-1), False)
    print(is_prime(98766781), False)
    print(is_prime_best(98766781), False)
    print(time.time() - start)
    print(math.sqrt(98766781))

    n = 75
    print(list(n % d for d in range(2, int(math.sqrt(n)) + 1)))
