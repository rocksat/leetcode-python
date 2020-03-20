#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution_Bottom_Up:
    def __init__(self):
        self.list = None

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        self.list = head
        return self.sorted_list_to_BST(0, n-1)

    def sorted_list_to_BST(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = start + (end - start) // 2
        left_child = self.sorted_list_to_BST(start, mid-1)
        node = TreeNode(self.list.val)
        node.left = left_child
        self.list = self.list.next
        right_child = self.sorted_list_to_BST(mid+1, end)
        node.right = right_child
        return node


class Solution_Top_Down:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.sorted_list_to_BST(head, None)

    def sorted_list_to_BST(self, head: ListNode, tail: ListNode) -> TreeNode:
        if head == tail:
            return None
        if head.next == tail:
            node = TreeNode(head.val)
            return node
        mid = tmp = head
        while tmp != tail and tmp.next != tail:
            mid = mid.next
            tmp = tmp.next.next
        node = TreeNode(mid.val)
        node.left = self.sorted_list_to_BST(head, mid)
        node.right = self.sorted_list_to_BST(mid.next, tail)
        return node


# @lc code=end
