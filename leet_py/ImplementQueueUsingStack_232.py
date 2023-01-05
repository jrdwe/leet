
class MyQueue:

    def __init__(self):
        self.inbox  = []
        self.outbox = []

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def pop(self) -> int:
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        
        return self.outbox.pop()

    def peek(self) -> int:
        if not self.outbox:
            return self.inbox[0]
        return self.outbox[-1]

    def empty(self) -> bool:
        return not self.outbox and not self.inbox
