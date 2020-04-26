#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
import copy


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return
        rows, cols = len(image), len(image[0])
        new_color_image = copy.deepcopy(image)
        curColor = new_color_image[sr][sc]
        if curColor == newColor:
            return new_color_image

        queue = [(sr, sc)]
        while queue:
            r, c = queue.pop(0)
            new_color_image[r][c] = newColor
            if 0 <= r + 1 < rows and 0 <= c < cols and new_color_image[
                    r + 1][c] == curColor:
                queue.append((r + 1, c))
            if 0 <= r - 1 < rows and 0 <= c < cols and new_color_image[
                    r - 1][c] == curColor:
                queue.append((r - 1, c))
            if 0 <= r < rows and 0 <= c + 1 < cols and new_color_image[r][
                    c + 1] == curColor:
                queue.append((r, c + 1))
            if 0 <= r < rows and 0 <= c - 1 < cols and new_color_image[r][
                    c - 1] == curColor:
                queue.append((r, c - 1))
        return new_color_image


class Solution_Recursion:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return

        new_color_image = copy.deepcopy(image)
        curColor = new_color_image[sr][sc]
        if curColor == newColor:
            return new_color_image

        self.dfs(new_color_image, sr, sc, curColor, newColor)
        return new_color_image

    def dfs(self, image: List[List[int]], sr: int, sc: int, curColor: int,
            newColor: int) -> None:
        rows, cols = len(image), len(image[0])
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols or image[sr][
                sc] != curColor:
            return

        image[sr][sc] = newColor
        self.dfs(image, sr + 1, sc, curColor, newColor)
        self.dfs(image, sr - 1, sc, curColor, newColor)
        self.dfs(image, sr, sc + 1, curColor, newColor)
        self.dfs(image, sr, sc - 1, curColor, newColor)


# @lc code=end
