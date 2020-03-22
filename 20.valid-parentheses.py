#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def __init__(self):
        self.lut = {'[': ']', '{': '}', '(': ')'}

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.lut:
                stack.append(c)
            elif not stack or self.lut[stack.pop(-1)] != c:
                return False
        return True if not stack else False


# @lc code=end
