class MyQueue:

    def __init__(self):
        self.stack = []
        self.tempStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.tempStack.append(self.stack.pop())
        res = self.tempStack.pop()
        while self.tempStack:
            self.stack.append(self.tempStack.pop())
        return res


    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()