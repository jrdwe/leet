
class MyStack:

    def __init__(self):
        self.inbox = Deque()

    def push(self, x: int) -> None:
        l = len(self.inbox)
        self.inbox.append(x)
        for i in range(l):
            val = self.inbox.pop()
            self.inbox.append(val)

    def pop(self) -> int:
        return self.inbox.pop()

    def top(self) -> int:
        val = self.inbox.pop()
        self.inbox.append(val)
        return val

    def empty(self) -> bool:
        return len(self.inbox) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
