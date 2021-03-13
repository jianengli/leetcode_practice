class MaxQueue:

    def __init__(self):
        from collections import deque
        self.deque = deque()
        self.queue = []

    def max_value(self) -> int:
        if self.deque: return self.deque[0]
        else: return -1


    def push_back(self, value: int) -> None:
    
        self.queue.append(value)
        # 此为最简形式，不需要考虑deque是否为空，因为都需要对deque加入value
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value) 

    def pop_front(self) -> int:
        if not self.queue: return -1
        else:
            
            if self.deque and self.queue[0] == self.deque[0]:
                self.deque.popleft()
            t = self.queue[0]
            del self.queue[0]
            return t



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()