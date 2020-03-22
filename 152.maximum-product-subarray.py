#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = [1] * (len(nums) + 1)
        min_product = [1] * (len(nums) + 1)
        res = -sys.maxsize - 1
        for i, num in enumerate(nums):
            max_product[i] = max(
                max(max_product[i - 1] * num, min_product[i - 1] * num), num)
            min_product[i] = min(
                min(max_product[i - 1] * num, min_product[i - 1] * num), num)
            res = max(res, max_product[i])
        return res


# @lc code=end
