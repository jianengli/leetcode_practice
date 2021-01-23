class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            dif = prices[i+1] - prices[i]
            if dif > 0:
                res += dif
        return res

