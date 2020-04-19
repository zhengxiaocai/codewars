"""
https://www.codewars.com/kata/5966847f4025872c7d00015b/train/python

"""


def average_string(s):
    nums = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    try:
        num = int(sum(nums[i] for i in s.split(' ')) / len(s.split(' ')))
        for key, value in nums.items():
            if num  == value:
                return key
    except KeyError:
        return 'n/a'


def average_string_best(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    try:
        return nums[sum(nums.index(i) for i in s.split()) // len(s.split())]
    except Exception:
        return 'n/a'


if __name__ == '__main__':
    print(average_string_best("zero nine five two") == "four")
    print(average_string_best("four six two three") == "three")
    print(average_string_best("one two three four five") == "three")
    print(average_string_best("five four") == "four")
    print(average_string_best("zero zero zero zero zero") == "zero")
    print(average_string_best("one one eight one") == "two")
    print(average_string_best("one") == "one")
    print(average_string_best("") == "n/a")
    print(average_string_best("ten") == "n/a")
    print(average_string_best("pippi") == "n/a")

