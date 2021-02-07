class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_cost = float('inf')
        for i in range(len(prices)):
            min_cost = min(prices[i],min_cost)
            max_prof = max(max_prof, prices[i] - min_cost)
        return max_prof