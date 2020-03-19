#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.sorted_array_to_bst(nums, 0, len(nums) - 1)

    def sorted_array_to_bst(self, nums: List[int], start: int,
                            end: int) -> TreeNode:
        if start > end:
            return None
        mid = start + (end - start) // 2
        node = TreeNode(nums[mid])
        node.left = self.sorted_array_to_bst(nums, start, mid - 1)
        node.right = self.sorted_array_to_bst(nums, mid + 1, end)
        return node


# @lc code=end
