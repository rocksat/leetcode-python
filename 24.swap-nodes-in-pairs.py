#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = head.next
        head.next = self.swapPairs(node.next)
        node.next = head
        return node


class Solution_Iteration:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr and curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr
            prev.next = tmp

            prev = curr
            curr = curr.next
        return dummy.next


# @lc code=end
