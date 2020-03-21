#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        return self.dfs_bottom_up(root, None)

    def dfs_bottom_up(self, p: TreeNode, parent: TreeNode) -> TreeNode:
        if not p:
            return parent
        root = self.dfs_bottom_up(p.left, p)
        p.left = parent if not parent else parent.right
        p.right = parent
        return root


class Solution_Top_Down:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        p, parent, parent_right = root, None, None
        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
        return parent


# @lc code=end
