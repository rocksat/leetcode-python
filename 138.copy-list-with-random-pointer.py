#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dummy = Node(-1)
        lut = dict()
        p1 = head
        p2 = Node(p1.val)
        lut[p1] = p2
        dummy.next = p2
        while p1.next:
            p2.next = Node(p1.next.val)
            lut[p1.next] = p2.next
            p1 = p1.next
            p2 = p2.next

        p1 = head
        p2 = dummy.next
        while p1:
            if p1.random:
                p2.random = lut[p1.random]
            else:
                p2.random = None
            p1 = p1.next
            p2 = p2.next
        return dummy.next


class Solution_HashMap:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        lut = dict()
        p1 = head
        p2 = Node(head.val)
        lut[p1] = p2

        while p1:
            if p1.next:
                if p1.next in lut:
                    p2.next = lut[p1.next]
                else:
                    p2.next = Node(p1.next.val)
                    lut[p1.next] = p2.next
            if p1.random:
                if p1.random in lut:
                    p2.random = lut[p1.random]
                else:
                    p2.random = Node(p1.random.val)
                    lut[p1.random] = p2.random
            p1 = p1.next
            p2 = p2.next
        return lut[head]


# @lc code=end
