#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution_LUT:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lut = [0] * 256
        max_len = 0
        i = j = 0
        while j < len(s):
            while lut[ord(s[j])] != 0:
                lut[ord(s[i])] -= 1
                i += 1
            lut[ord(s[j])] += 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len


class Solution_Brute_Force:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        max_len = 0
        for j in range(len(s) + 1):
            for i in range(j):
                if not self.containRepetition(s[i:j]):
                    max_len = max(max_len, j - i)
        return max_len

    @staticmethod
    def containRepetition(string: str) -> bool:
        return len(set(string)) != len(string)


# @lc code=end
