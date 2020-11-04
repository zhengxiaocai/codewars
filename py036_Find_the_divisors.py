# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python


def divisors(integer):
    result = [i for i in range(2, integer) if integer % i == 0]
    return result if result else f'{integer} is prime'


def divisors_best(integer):
    # TODO：这个有点猛
    return [i for i in range(2, integer) if integer % i == 0] or f'{integer} is prime'


if __name__ == '__main__':
    print(divisors_best(15), [3, 5])
    print(divisors_best(12), [2, 3, 4, 6])
    print(divisors_best(13), "13 is prime")
