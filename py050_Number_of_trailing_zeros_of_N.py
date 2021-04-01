def zeros(n):
    result = 0
    s = 1
    for i in range(1, n + 1):
        s = s * int()
        if str(s // 10).isdigit() and s // 10 != 0:
            result += 1
        s = s % 10
    return result


if __name__ == '__main__':
    print(zeros(0), 0, "Testing with n = 0")
    print(zeros(6), 1, "Testing with n = 6")
    print(zeros(30), 7, "Testing with n = 30")

    print(10 % 10)
    print(11 % 10)
    print(0 % 10)
    print('1'.isdigit())
    print('1.2'.isdigit())
