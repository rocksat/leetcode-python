#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = dict()
        for idx, val in enumerate(nums):
            if target - val in ht:
                return [idx, ht[target - val]]
            ht[val] = idx


# @lc code=end
