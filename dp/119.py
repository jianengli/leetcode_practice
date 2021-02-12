# 1 时间复杂度O(n^2)，空间复杂度O(n) dp
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1: return [1,1] 
        dp = [ 1 for _ in range(rowIndex+1)]
        for i in range(rowIndex):
            l = [ z for z in range(1,i+1)]
            for j in reversed(l):
                dp[j] = dp[j-1]+dp[j]
            print(dp)
            # dp[j+1] = 1
        return dp

# 2 公式 时间复杂度O(n)，空间复杂度O(n)。
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1] * (rowIndex + 1)
        for i in range(1, len(arr) - 1):
            arr[i] = arr[i - 1] * (rowIndex - i + 1) // i
        return arr

作者：coldme-2
链接：https://leetcode-cn.com/problems/pascals-triangle-ii/solution/dong-tai-gui-hua-tong-xiang-gong-shi-by-tn2dh/ 
