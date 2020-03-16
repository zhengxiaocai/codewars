"""
https://www.codewars.com/kata/515decfd9dcfc23bb6000006/python
给一个字符串，判断是否是ipv4的IP
难点：判断'56 '，'045'不合法。（因为这两个都可以用int()转化）
"""


def is_valid_IP(s):
    return s.count('.') == 3 and all(i.isdigit() and 0<=int(i)<=255 and i==str(int(i)) for i in s.split('.'))


if __name__ == '__main__':
    print(is_valid_IP('12.255.56.1'), True)
    print(is_valid_IP(''), False)
    print(is_valid_IP('abc.def.ghi.jkl'), False)
    print(is_valid_IP('123.456.789.0'), False)
    print(is_valid_IP('12.34.56'), False)
    print(is_valid_IP('12.34.56 .1'), False)
    print(is_valid_IP('12.34.56.-1'), False)
    print(is_valid_IP('123.045.067.089'), False)
    print(is_valid_IP('127.1.1.0'), True)
    print(is_valid_IP('0.0.0.0'), True)
    print(is_valid_IP('0.34.82.53'), True)
    print(is_valid_IP('192.168.1.300'), False)

    print('56 '.isdigit())
    print('045'.isdigit())

    """
    总结：
        1.'45 '的合法性，可以用 s.isdigit() 来判断，因为它有一个空格。
            通过这个判断完，还可以防止字母混入接下来的判断，出异常。
        2.'045'的合法性，可以用 str(int(s)) == s 来判断
        3.all()
    """
