#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, rows, cols)
                    count += 1
        return count

    def dfs(self, grid: List[List[str]], i: int, j: int, rows: int,
            cols: int) -> None:
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, rows, cols)
        self.dfs(grid, i - 1, j, rows, cols)
        self.dfs(grid, i, j + 1, rows, cols)
        self.dfs(grid, i, j - 1, rows, cols)


# @lc code=end
