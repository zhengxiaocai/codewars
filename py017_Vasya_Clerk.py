"""
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
"""


def tickets(people):
    money = { 25: 0, 50: 0}
    for p in people:
        if p == 25:
            money[25] += 1
        elif p == 50:
            if money[25] < 1:
                return 'NO'
            else:
                money[25] -= 1
                money[50] += 1
        elif p == 100:
            if money[25] == 0 or (money[25] in [1, 2] and money[50] == 0):
                return 'NO'
            else:
                if money[50] >= 1:
                    money[50] -= 1
                    money[25] -= 1
                else:
                    money[25] -= 3
    return 'YES'


if __name__ == '__main__':
    print(tickets([25, 25, 50]) == "YES")
    print(tickets([25, 100]) == "NO")
    print(tickets([25, 50]) == "YES")
    print(tickets([25, 50, 25, 100]) == "YES")
    print(tickets([25, 25, 25, 100]) == "YES")
    print(tickets([25, 50, 25, 50, 100]) == "NO")





