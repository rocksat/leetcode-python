#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start


class Solution_Set:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()


class Solution_Bit_Manipulation:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


# @lc code=end
