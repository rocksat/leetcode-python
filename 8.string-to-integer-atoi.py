#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.MAX_INT = 2147483647
        self.MIN_INT = -2147483648
        self.maxDiv10 = int(self.MAX_INT / 10)

    def myAtoi(self, str: str) -> int:
        i, n = 0, len(str)
        while i < n and str[i] == " ":
            i += 1
        sign = 1
        if i < n and str[i] == "+":
            i += 1
        elif i < n and str[i] == "-":
            sign *= -1
            i += 1
        num = 0
        while i < n and str[i].isdigit():
            digit = int(str[i])
            if num > self.maxDiv10 or (num == self.maxDiv10 and digit >= 8):
                return self.MAX_INT if sign == 1 else self.MIN_INT
            num = num * 10 + digit
            i += 1
        return sign * num


# @lc code=end
