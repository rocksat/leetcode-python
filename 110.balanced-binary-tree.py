#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.maxDepth(root) != -1

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        if leftDepth == -1:
            return -1
        rightDepth = self.maxDepth(root.right)
        if rightDepth == -1:
            return -1
        if abs(leftDepth - rightDepth) > 1:
            return -1
        return 1 + max(leftDepth, rightDepth)


class Solution_Brute_Force:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return abs(leftDepth - rightDepth) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# @lc code=end
