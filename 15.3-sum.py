#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        while i < (len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            i += 1
        return res


# @lc code=end
