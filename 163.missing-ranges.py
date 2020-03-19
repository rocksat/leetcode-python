#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#


# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int,
                          upper: int) -> List[str]:
        lower_bound = [lower] + [num + 1 for num in nums]
        upper_bound = [num - 1 for num in nums] + [upper]
        ranges = []
        for beg, end in zip(lower_bound, upper_bound):
            if beg == end:
                ranges.append("{}".format(beg))
            elif beg < end:
                ranges.append("{}->{}".format(beg, end))
        return ranges


class Solution_Linear_Scan:
    def findMissingRanges(self, nums: List[int], lower: int,
                          upper: int) -> List[str]:
        ranges = []
        prev = lower - 1
        nums.append(upper + 1)
        for val in nums:
            if val - prev >= 2:
                ranges.append(self.get_range(prev + 1, val - 1))
            prev = val
        return ranges

    @staticmethod
    def get_range(beg: int, end: int) -> str:
        if beg == end:
            return str(beg)
        return str(beg) + "->" + str(end)


# @lc code=end
