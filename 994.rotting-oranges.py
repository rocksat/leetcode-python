#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        queue = []
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append([r, c, 0])

        d = 0
        while queue:
            r, c, d = queue.pop(0)
            if 0 <= r - 1 < rows and 0 <= c < cols and grid[r - 1][c] == 1:
                grid[r - 1][c] = 2
                queue.append([r - 1, c, d + 1])
            if 0 <= r + 1 < rows and 0 <= c < cols and grid[r + 1][c] == 1:
                grid[r + 1][c] = 2
                queue.append([r + 1, c, d + 1])
            if 0 <= r < rows and 0 <= c - 1 < cols and grid[r][c - 1] == 1:
                grid[r][c - 1] = 2
                queue.append([r, c - 1, d + 1])
            if 0 <= r < rows and 0 <= c + 1 < cols and grid[r][c + 1] == 1:
                grid[r][c + 1] = 2
                queue.append([r, c + 1, d + 1])

        if any(1 in row for row in grid):
            return -1
        return d


# @lc code=end
