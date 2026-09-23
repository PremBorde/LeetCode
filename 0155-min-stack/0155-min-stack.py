class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([value,value])
        else:
            mini = min(self.stack[-1][1],value)
            self.stack.append([value,mini])
        return

    def pop(self) -> None:
        if len(self.stack) == 0:
            return 0
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()