class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2]: return n
        dp = [1,2] + [0 for _ in range(n-2)]
        for i in range(2,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1] 