#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(1, len(height) - 1):
            water = max(min(left_max[i], right_max[i]) - height[i], 0)
            res += water
        return res


class Solution__Brute_Force:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        for i in range(1, len(height) - 1):
            left_max, right_max = 0, 0
            for l in range(i):
                left_max = max(left_max, height[l])
            for r in range(i + 1, len(height)):
                right_max = max(right_max, height[r])
            water = max(min(left_max, right_max) - height[i], 0)
            res += water
        return res


# @lc code=end
