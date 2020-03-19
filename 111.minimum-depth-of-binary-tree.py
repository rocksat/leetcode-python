#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution_BFS:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = []
        q.append(root)
        right_most = root
        depth = 1
        while q:
            node = q[0]
            q.pop(0)
            if not node.left and not node.right:
                break
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node == right_most:
                depth += 1
                right_most = node.right if node.right else node.left
        return depth


class Solution_Recursion:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


# @lc code=end
