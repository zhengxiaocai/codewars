"""
题目如下：
给您一个字符串数组s和一个整数k。您的任务是返回由数组中的k个连续字符串组成的最长字符串。
例子：longest_consec（["abigail"，"theta"，"form"，"libe"，"zas"，"theta"，"abigail"]，2）->"abigailtheta"
n是字符串数组的长度，如果n = 0 or k > n or k <= 0返回""
注意：连续的字符串
"""


def longest_consec(s, k):
    # 第一种：
    # result = []
    # if 0 <= k <= len(strarr):
    #     for i in range(len(strarr) - k + 1):
    #         result.append(''.join(strarr[i:i+k]))
    #     return max(result, key=lambda x:len(x))
    # return ''

    # 第二种：
    # return max([''.join(s[i:i+k]) for i in range(len(s)-k+1)], key=lambda x:len(x)) if 0 <= k <= len(s) else ''

    # 第三种：优化lambda
    return max([''.join(s[i:i + k]) for i in range(len(s) - k + 1)], key=len) if 0 <= k <= len(s) else ''


if __name__ == '__main__':
    # 测试
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta")
    print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) ==
            "oocccffuucccjjjkkkjyyyeehh")
    print(longest_consec([], 3) == "")
    print(longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) ==
        "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
    print(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2) ==
            "wlwsasphmxxowiaxujylentrklctozmymu")
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == "")
    print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz")
    print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15) == "")
    print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0) == "")

