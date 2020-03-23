#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = list(set(nums))
        return len(nums)


class Solution_Two_Points:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        idx = 0
        for j in range(len(nums)):
            if nums[j] != nums[idx]:
                nums[idx + 1] = nums[j]
                idx += 1
        return idx + 1


# @lc code=end
