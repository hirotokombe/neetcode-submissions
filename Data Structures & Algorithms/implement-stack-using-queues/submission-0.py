class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.size += 1
    
    def pop(self) -> int:
        currentSize = self.size
        while self.size > 1:
            val = self.queue1.popleft()
            self.queue2.append(val)
            self.size-=1
        popVal = self.queue1.popleft()

        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp
        self.size = currentSize - 1
        return popVal

    def top(self) -> int:
        currentSize = self.size
        topVal = 0
        while self.size > 0:
            val = self.queue1.popleft()
            self.queue2.append(val)
            if self.size == 1:
                topVal = val
            self.size-=1

        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp
        self.size = currentSize
        return topVal

    def empty(self) -> bool:
        return True if self.size == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()