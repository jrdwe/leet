
class MinStack:
    def __init__(self):
        self.stack = []
        self.min   = float('inf')

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        self.min = min(self.min, val)

    def pop(self) -> None:
        self.min = self.stack[-1][1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min
        
