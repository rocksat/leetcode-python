#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign, ret = 1, 0
        if x < 0:
            sign *= -1
            x *= -1
        while x:
            ret = ret * 10 + x % 10
            x //= 10

        return 0 if ret > pow(2, 31) else ret * sign


# @lc code=end
