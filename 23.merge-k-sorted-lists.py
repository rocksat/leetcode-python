#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue


class Solution_Priority_Queue:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = dummy = ListNode()
        p = PriorityQueue()
        for l in lists:
            if l:
                p.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            head.next = node
            head = head.next
            if node.next:
                p.put((node.next.val, node.next))
        return dummy.next


class Solution_DIVIDE_CONQUER:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return []
        start, end = 0, len(lists) - 1
        return self.merge_helper(lists, start, end)

    def merge_helper(self, lists: List[ListNode], start: int,
                     end: int) -> ListNode:
        if start == end:
            return lists[start]
        mid = int(start + (end - start) // 2)
        l1 = self.merge_helper(lists, start, mid)
        l2 = self.merge_helper(lists, mid + 1, end)
        return self.merge_two_lists(l1, l2)

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return dummy.next


# @lc code=end
