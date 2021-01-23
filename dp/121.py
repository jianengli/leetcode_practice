method1: double pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        pointer1 = 0
        min_value = 9999
        max_value = -9999
        for pointer2 in range(len(prices)):
            if prices[pointer2] == min(prices[pointer2],min_value):
                min_value = prices[pointer2]
                pointer1 = pointer2 # 可以去掉
            max_value = max(max_value, prices[pointer2] - min_value)
        return max_value
method 2: dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        cur = 0 # 最大利润必然为 非负数；因为可以不买入
        min_price = float('inf')
        for i in range(0,len(prices)):
            min_price = min(min_price, prices[i])
            cur = max(cur, prices[i] - min_price)
        return cur