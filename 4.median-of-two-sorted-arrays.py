#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start

import sys


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        half_len = (m + n + 1) // 2
        start, end = 0, m
        while start <= end:
            i = start + (end - start) // 2
            j = half_len - i
            max_left_nums1 = nums1[i - 1] if i != 0 else -sys.maxsize - 1
            max_left_nums2 = nums2[j - 1] if j != 0 else -sys.maxsize - 1
            min_right_nums1 = nums1[i] if i < m else sys.maxsize
            min_right_nums2 = nums2[j] if j < n else sys.maxsize

            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (m + n) % 2 != 0:
                    return max(max_left_nums1, max_left_nums2)
                else:
                    return (max(max_left_nums1, max_left_nums2) +
                            min(min_right_nums1, min_right_nums2)) / 2
            elif max_left_nums1 > min_right_nums2:
                end = i - 1
            else:
                start = i + 1


# i should be able to pick 0 or m. So the while loop criteria is start <= end


# @lc code=end
