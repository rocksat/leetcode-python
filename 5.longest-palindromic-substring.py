#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_length = 0, 0
        for i in range(len(s)):
            length1 = self.expand_around_center(s, i, i)
            length2 = self.expand_around_center(s, i, i + 1)
            length = max(length1, length2)
            if length > max_length:
                start = i - int((length - 1) / 2)
                max_length = length
        return s[start:start + max_length]

    @staticmethod
    def expand_around_center(s: str, left: int, right: int) -> int:
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1


class Solution_DP:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        start, end = 0, 0

        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    is_palindrome[i][j] = True
                elif i + 1 == j:
                    is_palindrome[i][j] = s[i] == s[j]
                elif s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True

                if is_palindrome[i][j] and j - i > end - start:
                    start = i
                    end = j
        return s[start:end + 1]


class Solution_Brute_Force:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        curr_longest_palindrone = ""
        for j in range(n + 1):
            for i in range(j):
                if self.is_palidrome(
                        s[i:j]) and j - i > len(curr_longest_palindrone):
                    curr_longest_palindrone = s[i:j]
        return curr_longest_palindrone

    @staticmethod
    def is_palidrome(s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


# @lc code=end
