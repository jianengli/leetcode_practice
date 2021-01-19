class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[n-1][m-1]