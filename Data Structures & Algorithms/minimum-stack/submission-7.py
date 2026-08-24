class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimum = val

        value = val - self.minimum
        if value < 0:
            self.minimum = val
        self.stack.append(value)

    def pop(self) -> None:
        if not self.stack:
            return

        peek = self.stack.pop()
        if peek < 0:
            self.minimum = self.minimum - peek
        
    def top(self) -> int:
        top = self.stack[-1]
        if top < 0: 
            return self.minimum
        else:
            return top + self.minimum

    def getMin(self) -> int:
        return self.minimum
            

