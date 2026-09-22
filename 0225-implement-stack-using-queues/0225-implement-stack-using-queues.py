from collections import deque
class MyStack:

    def __init__(self):
        self.myStack = deque()

    def push(self, x: int) -> None:
        self.myStack.append(x)
        for _ in range(len(self.myStack)-1):
            self.myStack.append(self.myStack.popleft())

    def pop(self) -> int:
        x = self.myStack.popleft()
        return x

    def top(self) -> int:
        x = self.myStack[0]
        return x

    def empty(self) -> bool:
        if len(self.myStack) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()