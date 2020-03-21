#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            rem = count % 3
            if i == 31 and rem:
                res -= 1 << 31
            else:
                res += rem * (1 << i)
        return res


class Solution_HashTable:
    def singleNumber(self, nums: List[int]) -> int:
        lut = dict()
        for num in nums:
            if num not in lut:
                lut[num] = 1
            else:
                lut[num] += 1
        for num, count in lut.items():
            if count == 1:
                return num


# @lc code=end
