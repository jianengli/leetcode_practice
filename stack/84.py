# 1. 入栈：不确定当前元素勾勒出最大矩形面积，出栈，能确定当前元素勾勒出最大矩形面积
# 2. 何时出栈：能看到的元素严格小于栈顶元素的时候，出栈，进而计算栈顶元素能勾勒出的最大矩形面积
# 3. 当前矩形的宽度 = 当前遍历到元素的下标 与 新出栈元素的下标差 减 1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: