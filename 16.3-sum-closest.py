#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = None
        i = 0
        while i < (len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if res == None or abs(total - target) < abs(res - target):
                    res = total
                if total <= target:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                else:
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
            i += 1
        return res


# @lc code=end
