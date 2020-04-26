#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        right_max = [0] * len(prices)
        right_max[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], prices[i])

        res = 0
        for i, price in enumerate(prices):
            res = max(right_max[i] - price, res)
        return res


# @lc code=end
