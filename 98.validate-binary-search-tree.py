#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution_Traverse:
    def __init__(self):
        self.prev = -sys.maxsize - 1

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        if not self.isValidBST(root.right):
            return False
        return True


class Solution_Brute_Force:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left:
            precessor = root.left
            while precessor.right:
                precessor = precessor.right
            if precessor.val >= root.val:
                return False
        if root.right:
            successor = root.right
            while successor.left:
                successor = successor.left
            if successor.val <= root.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)


class Solution_Top_Down:
    def isValidBST(self, root: TreeNode) -> bool:
        upper = sys.maxsize
        lower = -sys.maxsize - 1
        return self.helper(root, lower, upper)

    def helper(self, root: TreeNode, lower: int, upper: int) -> bool:
        if not root:
            return True
        return (lower < root.val < upper) \
            and self.helper(root.left, lower, root.val) \
            and self.helper(root.right, root.val, upper)


# @lc code=end
