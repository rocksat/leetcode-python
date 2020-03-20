#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution:
    def __init__(self) -> None:
        self.max_path_sum = -sys.maxsize - 1

    def maxPathSum(self, root: TreeNode) -> int:
        self.node_max_path_sum(root)
        return self.max_path_sum

    def node_max_path_sum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_sum = self.node_max_path_sum(root.left)
        right_sum = self.node_max_path_sum(root.right)
        ret = max(left_sum, right_sum) + root.val
        self.max_path_sum = max(left_sum + right_sum + root.val,
                                self.max_path_sum)
        return ret if ret > 0 else 0


# @lc code=end
