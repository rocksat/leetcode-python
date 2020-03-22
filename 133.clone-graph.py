#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        lut = dict()
        queue = []
        queue.append(node)
        node_copy = Node(node.val)
        lut[node] = node_copy
        while queue:
            tmp = queue[0]
            queue.pop(0)
            for neighbor in tmp.neighbors:
                if neighbor in lut:
                    lut[tmp].neighbors.append(lut[neighbor])
                else:
                    neighbor_copy = Node(neighbor.val)
                    lut[tmp].neighbors.append(neighbor_copy)
                    lut[neighbor] = neighbor_copy
                    queue.append(neighbor)
        return node_copy


class Solution_Recursion:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        lut = dict()
        return self.dfs(node, lut)

    def dfs(self, node: 'Node', lut: dict) -> 'Node':
        if node in lut:
            return lut[node]
        node_copy = Node(node.val)
        lut[node] = node_copy
        for neighbor in node.neighbors:
            node_copy.neighbors.append(self.dfs(neighbor, lut))
        return node_copy


# @lc code=end
