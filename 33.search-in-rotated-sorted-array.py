#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] < nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


# @lc code=end
