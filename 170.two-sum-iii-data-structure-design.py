#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#


# @lc code=start
class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = dict()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.ht:
            self.ht[number] += 1
        else:
            self.ht[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for number, count in self.ht.items():
            delta = value - number
            if delta in self.ht and (delta != number or count >= 2):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end
