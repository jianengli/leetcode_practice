class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.helper and x <= self.helper[-1] or not self.helper: # <= 的 = 不要忘记，否则最小元素出现几次的话，会进入辅助栈的元素变少
            self.helper.append(x) 

    def pop(self) -> None:
        t= self.stack.pop()
        if self.helper and t == self.helper[-1]: # if t in self.helper: 会报错，因为无法确定数据栈弹出的元素和辅助栈最后一个元素一致
            self.helper.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        if self.helper:
            return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()