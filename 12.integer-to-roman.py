#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def __init__(self):
        self.integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.roman = [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV',
            'I'
        ]

    def intToRoman(self, num: int) -> str:
        res = ""
        i = 0
        while num > 0:
            k = num // self.integer[i]
            for _ in range(k):
                res += self.roman[i]
                num -= self.integer[i]
            i += 1
        return res


# @lc code=end
