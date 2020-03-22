#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def __init__(self):
        self.lut = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        prev, total = 0, 0
        for c in s:
            curr = self.lut[c]
            if curr > prev:
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total


# @lc code=end
