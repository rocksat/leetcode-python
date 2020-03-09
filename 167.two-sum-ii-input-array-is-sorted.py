#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 1, n
        while i <= j:
            s = numbers[i - 1] + numbers[j - 1]
            if s == target:
                return [i, j]
            elif s < target:
                i += 1
            else:
                j -= 1


# @lc code=end
