#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution_Stack:
    def reverseWords(self, s: str) -> str:
        stack = []
        for word in s.strip().split():
            stack.append(word)
        return " ".join(stack[::-1])


class Solution_TwoPointers:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i, j = len(s) - 1, len(s)
        res = ""
        while i >= 0:
            if s[i] == " ":
                j = i
            elif i == 0:
                res += s[i:j]
            elif s[i - 1] == " ":
                res += s[i:j]
                res += " "
            i -= 1
        return res


# @lc code=end
