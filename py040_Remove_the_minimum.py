# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python


def remove_smallest(numbers):
    number = numbers[:]
    min_obj = min(number, default=None)
    if min_obj:
        number.remove(min_obj)
    return number


def remove_smallest_best(numbers):
    number = numbers[:]
    if number:
        number.remove(min(number))
    return number


if __name__ == '__main__':
    print(remove_smallest_best([1, 2, 3, 4, 5]) == [2, 3, 4, 5])
    print(remove_smallest_best([5, 3, 2, 1, 4]) == [5, 3, 2, 4])
    print(remove_smallest_best([1, 2, 3, 1, 1]) == [2, 3, 1, 1])
    print(remove_smallest_best([]) == [])
    print(
        remove_smallest_best([101, 202, 253, 135, 394, 240, 180, 104, 354]) == [202, 253, 135, 394, 240, 180, 104, 354])

    print(min([], default=None))

    """
    a = []
    print(a.remove(min(a)))
    
    Traceback (most recent call last):
        File "/Users/yuan/PythonProject/codewars/py040_Remove_the_minimum.py", line 28, in <module>
            print(a.remove(min(a)))
    ValueError: min() arg is an empty sequence
    """

    """
    知识点：
    min() 方法可以添加default
    list.remove(value)    是在本身上改
    min([]) 会报错
    """
