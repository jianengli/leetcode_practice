class CQueue:

    def __init__(self):
        self.head_stack = []
        self.tail_stack = []

    def appendTail(self, value: int) -> None:
        self.head_stack.append(value)
        # 复杂了
        # if self.tail_stack:
        #     self.head_stack.append(value)
        # else: 
        #     self.head_stack.append(value)
        #     while self.head_stack: 
        #         self.tail_stack.append(self.head_stack.pop())  
        #         print(self.tail_stack)


    def deleteHead(self) -> int:
        if self.tail_stack: 
            return self.tail_stack.pop()
        else: 
            while self.head_stack: 
                self.tail_stack.append(self.head_stack.pop())   
            if self.tail_stack: 
                return self.tail_stack.pop()
            else:
                return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()