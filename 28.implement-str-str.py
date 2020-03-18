#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        while i <= len(haystack) - len(needle):
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len(needle):
                return i
            i += 1
        return -1


# @lc code=end
