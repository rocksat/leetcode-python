#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#


# @lc code=start
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        count = 0
        i = j = int(0)
        while i < m and j < n:
            if s[i] != t[j]:
                if count == 1:
                    return False
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1
                count += 1
            else:
                i += 1
                j += 1
        if i < m or j < n:
            count += 1

        return count == 1


# @lc code=end
