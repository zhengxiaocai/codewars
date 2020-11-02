# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python


def divisors(integer):
    result = [i for i in range(2, integer) if integer % i == 0]
    return result if result else f'{integer} is prime'


if __name__ == '__main__':
    print(divisors(15), [3, 5])
    print(divisors(12), [2, 3, 4, 6])
    print(divisors(13), "13 is prime")
