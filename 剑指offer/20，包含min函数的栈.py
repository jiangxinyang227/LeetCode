"""
给定一个栈，给出返回其最小值函数，需要O（1）时间实现
解题思路：用一个最小栈来存储无重复排好序的元素
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or self.getMin() >= x:
            self.min_stack.append(x)

    def pop(self) -> None:
        pop_val = self.stack.pop()
        if self.min_stack != [] and pop_val == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]


s = Stack()
s.push(3)
print(s.min())
s.push(1)
s.push(2)
print(s.min())
s.push(1)
print(s.min())
s.pop()
s.pop()
print(s.min())