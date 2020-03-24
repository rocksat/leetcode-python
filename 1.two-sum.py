#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lut = dict()
        for idx, num in enumerate(nums):
            if target - num in lut:
                return [idx, lut[target - num]]
            else:
                lut[num] = idx


class Solution_HashTable:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = dict()
        for idx, val in enumerate(nums):
            if target - val in ht:
                return [idx, ht[target - val]]
            ht[val] = idx


# @lc code=end
