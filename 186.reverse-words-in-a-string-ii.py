#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#

# @lc code=start


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = ' '.join(''.join(s).split()[::-1])


class Solution_Reverse:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        i = j = 0
        while j <= len(s):
            if j == len(s) or s[j] == " ":
                self.reverse(s, i, j - 1)
                i = j + 1
            j += 1

    def reverse(self, s: List[str], start: int, end: int) -> None:
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


# @lc code=end
