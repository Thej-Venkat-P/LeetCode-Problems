# url: https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(0)
        elif val < self.stack[self.min_stack[-1]]:
            self.min_stack.append(len(self.stack)-1)

    def pop(self) -> None:
        self.stack.pop()
        if self.min_stack[-1] == len(self.stack):
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_stack[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()