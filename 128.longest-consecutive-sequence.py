#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for num in nums:
            l = r = 0
            while (num + l) in s:
                l -= 1
            while (num + r) in s:
                r += 1
            max_len = max(max_len, r - l - 1)
        return max_len


# @lc code=end
