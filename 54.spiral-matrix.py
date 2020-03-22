#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return None
        res = []
        beginX, endX = 0, len(matrix[0]) - 1
        beginY, endY = 0, len(matrix) - 1
        while True:
            for i in range(beginX, endX + 1):
                res.append(matrix[beginY][i])
            beginY += 1
            if beginY > endY:
                break
            for i in range(beginY, endY + 1):
                res.append(matrix[i][endX])
            endX -= 1
            if beginX > endX:
                break
            for i in range(endX, beginX - 1, -1):
                res.append(matrix[endY][i])
            endY -= 1
            if beginY > endY:
                break
            for i in range(endY, beginY - 1, -1):
                res.append(matrix[i][beginX])
            beginX += 1
            if beginX > endX:
                break
        return res


# @lc code=end
