#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        ret = []
        i = 0
        while i < (len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < (len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total < target:
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        k += 1
                    elif total > target:
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        l -= 1
                    else:
                        tmp = [nums[i], nums[j], nums[k], nums[l]]
                        ret.append(tmp)
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k += 1
                        l -= 1
                j += 1
            i += 1
        return ret


# @lc code=end
