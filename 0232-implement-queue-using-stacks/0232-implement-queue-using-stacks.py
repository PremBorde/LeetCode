class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self) -> int:
        if len(self.st1) == 0:
            return 
        top = self.st1.pop()
        return top  

    def peek(self) -> int:
        if len(self.st1) == 0:
            return
        x = self.st1[-1]
        return x  
    
    def empty(self) -> bool:
        if len(self.st1) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()