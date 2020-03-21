#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff

        res = [0, 0]
        for num in nums:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


class Solution_HashTable:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lut = dict()
        res = []
        for num in nums:
            if num not in lut:
                lut[num] = 1
            else:
                lut[num] += 1
        for num, count in lut.items():
            if count == 1:
                res.append(num)
        return res


# @lc code=end
