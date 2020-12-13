class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, element in enumerate(prices):
            if i<len(prices)-1 and element<prices[i+1]:
                profit = profit + prices[i+1] - element
        return profit
        # O(n)