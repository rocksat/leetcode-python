#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
import sys


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = sys.maxsize
        for num in nums:
            min_num = min(min_num, num)
        return min_num


# @lc code=end
