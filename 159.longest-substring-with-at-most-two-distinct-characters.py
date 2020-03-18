#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lut = dict()
        max_len = 0
        i = j = 0
        while j < len(s):
            if s[j] in lut:
                lut[s[j]] += 1
            else:
                while len(lut) >= 2:
                    if lut[s[i]] > 1:
                        lut[s[i]] -= 1
                    else:
                        lut.pop(s[i])
                    i += 1
                lut[s[j]] = 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len


# @lc code=end
