class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:

        # dp[n-1][m-1] = [[0 for _ in range(m)] for _ in range(n)]
        m,n = len(grid),len(grid[0]) 

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0: 
                    grid[row][col] = grid[row][col]
                elif row != 0 and col == 0:
                    grid[row][col] =  ( grid[row-1][col]) + grid[row][col]
                elif row == 0 and col != 0:
                    grid[row][col] =  ( grid[row][col-1]) + grid[row][col]
                else:
                    grid[row][col] = max(grid[row-1][col],grid[row][col-1]) + grid[row][col]
        return grid[-1][-1]
# 以上代码逻辑清晰，和转移方程直接对应，但仍可提升效率：当 grid 矩阵很大时， i=0 或  j=0 的情况仅占极少数，相当循环每轮都冗余了一次判断。因此，可先初始化矩阵第一行和第一列，再开始遍历递推。 
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]

作者：jyd
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。