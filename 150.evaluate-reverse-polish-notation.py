#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def __init__(self):
        self.operator = ['+', '-', '*', '/']

    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            if token in self.operator:
                y = stack.pop(-1)
                x = stack.pop(-1)
                stack.append(self.eval(x, y, token))
            else:
                stack.append(int(token))
        return stack[-1]

    def eval(self, x: int, y: int, operator: str):
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        else:
            return int(float(x) / y)


# @lc code=end
