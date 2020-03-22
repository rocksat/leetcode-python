#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start

import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        max_sum = -sys.maxsize - 1
        for i, num in enumerate(nums):
            dp[i + 1] = max(dp[i] + num, num)
            max_sum = max(max_sum, dp[i + 1])
        return max_sum


class Solution_Brute_Force:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_array = [0]
        for num in nums:
            sum_array.append(sum_array[-1] + num)

        max_sum = -sys.maxsize - 1
        for j in range(len(nums) + 1):
            for i in range(j):
                curr_sum = sum_array[j] - sum_array[i]
                max_sum = max(max_sum, curr_sum)
        return max_sum


# @lc code=end
